import os

base = "Practice8"

folders = []

files = [
    f"{base}/phonebook.py",
    f"{base}/functions.sql",
    f"{base}/procedures.sql",
    f"{base}/config.py",
    f"{base}/connect.py",
    f"{base}/README.md"
]

# create folder
os.makedirs(base, exist_ok=True)

# create files
for file in files:
    with open(file, "w", encoding="utf-8") as f:
        f.write("")

print("Practice8 created successfully!")