contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"{name} - {info['phone']}")

def search_contact():
    search = input("Enter name or phone number to search: ").lower()
    found = False
    for name, info in contacts.items():
        if search in name.lower() or search in info['phone']:
            print(f"\nFound Contact:\nName: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        print("Leave a field empty to keep it unchanged.")
        phone = input(f"New phone (current: {contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"New email (current: {contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"New address (current: {contacts[name]['address']}): ") or contacts[name]['address']
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    print("📱 Welcome to the Contact Book App 📘")
    while True:
        print("\n--- MENU ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")

# Run the application
main()
