import psycopg2
from config import *

conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

cur = conn.cursor()

while True:
    print("\n1.Search")
    print("2.Upsert user")
    print("3.Show page")
    print("4.Delete user")
    print("5.Exit")

    choice = input("Choose: ")

    if choice == "1":
        p = input("Enter pattern: ")
        cur.execute("SELECT * FROM search_pattern(%s)", (p,))
        rows = cur.fetchall()

        for row in rows:
            print(row)

    elif choice == "2":
        name = input("Name: ")
        phone = input("Phone: ")

        cur.execute("CALL upsert_user(%s,%s)", (name, phone))
        conn.commit()
        print("Saved")

    elif choice == "3":
        lim = int(input("Limit: "))
        off = int(input("Offset: "))

        cur.execute("SELECT * FROM get_page(%s,%s)", (lim, off))
        rows = cur.fetchall()

        for row in rows:
            print(row)

    elif choice == "4":
        x = input("Username or phone: ")

        cur.execute("CALL delete_user(%s)", (x,))
        conn.commit()
        print("Deleted")

    elif choice == "5":
        break

cur.close()
conn.close()