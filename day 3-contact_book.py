# Contact Book — Python Lists
# Day 3 of learning in public

contacts = []

def add(): 
    name  = input("Name  : ").title()
    phone = input("Phone : ")
    contacts.append([name, phone])
    print(f"✓ {name} added.")

def view(): 
    if not contacts:
        print("No contacts.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c[0]} — {c[1]}")

def search():
    query   = input("Search : ").lower()
    results = [c for c in contacts if query in c[0].lower()]
    if results:
        for c in results:
            print(f"{c[0]} — {c[1]}")
    else:
        print("Not found.")

def delete():
    name  = input("Delete : ").title()
    match = [c for c in contacts if c[0] == name]
    if match:
        contacts.remove(match[0])
        print(f"✓ {name} deleted.")
    else:
        print("Not found.")

while True:
    print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")
    choice = input("> ")
    if   choice == "1": add()
    elif choice == "2": view()
    elif choice == "3": search()
    elif choice == "4": delete()
    elif choice == "5": break
