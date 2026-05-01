import csv
import json
import os
from connect import get_connection

PAGE_SIZE = 3

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue...")

def print_rows(rows, headers):
    if not rows:
        print("  (no results)")
        return
    widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            widths[i] = max(widths[i], len(str(val) if val is not None else ""))
    fmt = "  ".join(f"{{:<{w}}}" for w in widths)
    print(fmt.format(*headers))
    print("  ".join("-" * w for w in widths))
    for row in rows:
        print(fmt.format(*[str(v) if v is not None else "" for v in row]))

def get_or_create_group(cur, name):
    cur.execute("SELECT id FROM groups WHERE name = %s", (name,))
    row = cur.fetchone()
    if row:
        return row[0]
    cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id", (name,))
    return cur.fetchone()[0]

def add_contact():
    print("\n── Add Contact ──")
    username = input("Username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return
    email = input("Email (optional): ").strip() or None
    birthday = input("Birthday YYYY-MM-DD (optional): ").strip() or None
    print("Groups: Family / Work / Friend / Other (or type new)")
    group_name = input("Group (optional): ").strip() or None

    phones = []
    while True:
        phone = input("Phone number (leave blank to stop): ").strip()
        if not phone:
            break
        ptype = input("  Type (home/work/mobile): ").strip().lower()
        if ptype not in ("home", "work", "mobile"):
            ptype = "mobile"
        phones.append((phone, ptype))

    conn = get_connection()
    try:
        with conn:
            cur = conn.cursor()
            group_id = get_or_create_group(cur, group_name) if group_name else None
            try:
                cur.execute(
                    "INSERT INTO contacts (username, email, birthday, group_id) VALUES (%s,%s,%s,%s)",
                    (username, email, birthday, group_id)
                )
            except Exception as e:
                print(f"Error: {e}")
                return
            cur.execute("SELECT id FROM contacts WHERE username = %s", (username,))
            contact_id = cur.fetchone()[0]
            for phone, ptype in phones:
                cur.execute(
                    "INSERT INTO phones (contact_id, phone, type) VALUES (%s,%s,%s)",
                    (contact_id, phone, ptype)
                )
        print("Contact added.")
    finally:
        conn.close()

def search_contacts():
    query = input("\nSearch (name / email / phone): ").strip()
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM search_contacts(%s)", (query,))
        rows = cur.fetchall()
        print_rows(rows, ["Username", "Email", "Birthday", "Group", "Phones"])
    finally:
        conn.close()
    pause()

def filter_by_group():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT name FROM groups ORDER BY name")
        groups = [r[0] for r in cur.fetchall()]
        print("\nAvailable groups:", ", ".join(groups))
        group_name = input("Enter group name: ").strip()

        cur.execute("""
            SELECT c.username, c.email, c.birthday,
                   STRING_AGG(p.phone || ' (' || COALESCE(p.type,'?') || ')', ', ') AS phones
            FROM contacts c
            JOIN groups g ON g.id = c.group_id
            LEFT JOIN phones p ON p.contact_id = c.id
            WHERE g.name ILIKE %s
            GROUP BY c.username, c.email, c.birthday
            ORDER BY c.username
        """, (group_name,))
        rows = cur.fetchall()
        print_rows(rows, ["Username", "Email", "Birthday", "Phones"])
    finally:
        conn.close()
    pause()

def search_by_email():
    query = input("\nEmail keyword: ").strip()
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT username, email, birthday
            FROM contacts
            WHERE email ILIKE %s
            ORDER BY username
        """, (f"%{query}%",))
        rows = cur.fetchall()
        print_rows(rows, ["Username", "Email", "Birthday"])
    finally:
        conn.close()
    pause()

def list_sorted():
    print("\nSort by: 1) Name  2) Birthday  3) Date added")
    choice = input("Choice: ").strip()
    order = {"1": "c.username", "2": "c.birthday", "3": "c.created_at"}.get(choice, "c.username")
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(f"""
            SELECT c.username, c.email, c.birthday, g.name,
                   STRING_AGG(p.phone || ' (' || COALESCE(p.type,'?') || ')', ', ')
            FROM contacts c
            LEFT JOIN groups g ON g.id = c.group_id
            LEFT JOIN phones p ON p.contact_id = c.id
            GROUP BY c.username, c.email, c.birthday, g.name, c.created_at
            ORDER BY {order}
        """)
        rows = cur.fetchall()
        print_rows(rows, ["Username", "Email", "Birthday", "Group", "Phones"])
    finally:
        conn.close()
    pause()

def browse_paginated():
    conn = get_connection()
    page = 0
    try:
        while True:
            cur = conn.cursor()
            cur.execute("SELECT * FROM get_contacts_page(%s, %s)", (PAGE_SIZE, page * PAGE_SIZE))
            rows = cur.fetchall()
            clear()
            print(f"── Page {page + 1} ──")
            print_rows(rows, ["Username", "Email", "Birthday", "Group", "Phones"])
            print("\n[n] Next  [p] Prev  [q] Quit")
            cmd = input("> ").strip().lower()
            if cmd == "n":
                if len(rows) == PAGE_SIZE:
                    page += 1
                else:
                    print("Last page.")
            elif cmd == "p":
                page = max(0, page - 1)
            elif cmd == "q":
                break
    finally:
        conn.close()

def add_phone():
    name  = input("\nContact username: ").strip()
    phone = input("Phone number: ").strip()
    ptype = input("Type (home/work/mobile): ").strip().lower()
    if ptype not in ("home", "work", "mobile"):
        ptype = "mobile"
    conn = get_connection()
    try:
        with conn:
            cur = conn.cursor()
            cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
        print("Phone added.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
    pause()

def move_to_group():
    name  = input("\nContact username: ").strip()
    group = input("Group name: ").strip()
    conn = get_connection()
    try:
        with conn:
            cur = conn.cursor()
            cur.execute("CALL move_to_group(%s, %s)", (name, group))
        print(f'Moved "{name}" to group "{group}".')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
    pause()

def delete_contact():
    name = input("\nUsername to delete: ").strip()
    conn = get_connection()
    try:
        with conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM contacts WHERE username = %s", (name,))
            if cur.rowcount:
                print("Deleted.")
            else:
                print("Not found.")
    finally:
        conn.close()
    pause()

def export_json():
    filename = input("\nSave as (e.g. contacts.json): ").strip() or "contacts.json"
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT c.username, c.email, c.birthday::text, g.name AS grp,
                   JSON_AGG(
                       JSON_BUILD_OBJECT('phone', p.phone, 'type', p.type)
                   ) FILTER (WHERE p.phone IS NOT NULL) AS phones
            FROM contacts c
            LEFT JOIN groups g ON g.id = c.group_id
            LEFT JOIN phones p ON p.contact_id = c.id
            GROUP BY c.username, c.email, c.birthday, g.name
        """)
        rows = cur.fetchall()
        data = []
        for row in rows:
            data.append({
                "username": row[0],
                "email":    row[1],
                "birthday": row[2],
                "group":    row[3],
                "phones":   row[4] or []
            })
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Exported {len(data)} contacts to {filename}")
    finally:
        conn.close()
    pause()

def import_json():
    filename = input("\nJSON file path: ").strip()
    if not os.path.exists(filename):
        print("File not found.")
        pause()
        return
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)

    conn = get_connection()
    try:
        for item in data:
            username = item.get("username", "").strip()
            if not username:
                continue
            with conn:
                cur = conn.cursor()
                cur.execute("SELECT id FROM contacts WHERE username = %s", (username,))
                existing = cur.fetchone()
                if existing:
                    choice = input(f'"{username}" already exists. [s]kip / [o]verwrite? ').strip().lower()
                    if choice != "o":
                        continue
                    cur.execute("DELETE FROM contacts WHERE username = %s", (username,))

                group_id = get_or_create_group(cur, item["group"]) if item.get("group") else None
                cur.execute(
                    "INSERT INTO contacts (username, email, birthday, group_id) VALUES (%s,%s,%s,%s) RETURNING id",
                    (username, item.get("email"), item.get("birthday"), group_id)
                )
                contact_id = cur.fetchone()[0]
                for ph in (item.get("phones") or []):
                    cur.execute(
                        "INSERT INTO phones (contact_id, phone, type) VALUES (%s,%s,%s)",
                        (contact_id, ph.get("phone"), ph.get("type"))
                    )
        print("Import done.")
    finally:
        conn.close()
    pause()

def import_csv():
    filename = input("\nCSV file path: ").strip()
    if not os.path.exists(filename):
        print("File not found.")
        pause()
        return
    conn = get_connection()
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            added = 0
            for row in reader:
                username = row.get("username", "").strip()
                if not username:
                    continue
                with conn:
                    cur = conn.cursor()
                    cur.execute("SELECT id FROM contacts WHERE username = %s", (username,))
                    if cur.fetchone():
                        print(f'  Skipping duplicate "{username}"')
                        continue
                    group_id = get_or_create_group(cur, row.get("group")) if row.get("group") else None
                    cur.execute(
                        "INSERT INTO contacts (username, email, birthday, group_id) VALUES (%s,%s,%s,%s) RETURNING id",
                        (username, row.get("email") or None, row.get("birthday") or None, group_id)
                    )
                    contact_id = cur.fetchone()[0]
                    if row.get("phone"):
                        ptype = row.get("type", "mobile")
                        cur.execute(
                            "INSERT INTO phones (contact_id, phone, type) VALUES (%s,%s,%s)",
                            (contact_id, row["phone"], ptype)
                        )
                    added += 1
        print(f"Imported {added} contacts from CSV.")
    finally:
        conn.close()
    pause()

def main():
    while True:
        clear()
        print("═══════════════════════════")
        print("       PhoneBook TSIS 1    ")
        print("═══════════════════════════")
        print(" 1. Add contact")
        print(" 2. Search (name/email/phone)")
        print(" 3. Filter by group")
        print(" 4. Search by email")
        print(" 5. List sorted")
        print(" 6. Browse (paginated)")
        print(" 7. Add phone to contact")
        print(" 8. Move contact to group")
        print(" 9. Delete contact")
        print("10. Export to JSON")
        print("11. Import from JSON")
        print("12. Import from CSV")
        print(" 0. Exit")
        choice = input("\n> ").strip()

        if   choice == "1":  add_contact()
        elif choice == "2":  search_contacts()
        elif choice == "3":  filter_by_group()
        elif choice == "4":  search_by_email()
        elif choice == "5":  list_sorted()
        elif choice == "6":  browse_paginated()
        elif choice == "7":  add_phone()
        elif choice == "8":  move_to_group()
        elif choice == "9":  delete_contact()
        elif choice == "10": export_json()
        elif choice == "11": import_json()
        elif choice == "12": import_csv()
        elif choice == "0":  break

if __name__ == "__main__":
    main()