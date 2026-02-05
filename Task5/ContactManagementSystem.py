contacts = []

def show_menu():
    print("\n==============================")
    print("   CONTACT MANAGEMENT SYSTEM  ")
    print("==============================")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("==============================")

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"\n Contact {i}")
        print(f"Name    : {contact['name']}")
        print(f"Phone   : {contact['phone']}")
        print(f"Email   : {contact['email']}")
        print(f"Address : {contact['address']}")

def search_contact():
    print("\n--- Search Contact ---")
    keyword = input("Enter name or phone number to search: ")

    found = False
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print("\n Contact Found:")
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    print("\n--- Update Contact ---")
    phone = input("Enter phone number of contact to update: ")

    for contact in contacts:
        if contact['phone'] == phone:
            print("Enter new details (leave blank to keep old value)")
            new_name = input(f"New Name ({contact['name']}): ")
            new_email = input(f"New Email ({contact['email']}): ")
            new_address = input(f"New Address ({contact['address']}): ")

            if new_name:
                contact['name'] = new_name
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address

            print("Contact updated successfully!")
            return

    print("Contact not found.")

def delete_contact():
    print("\n--- Delete Contact ---")
    phone = input("Enter phone number of contact to delete: ")

    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")

def main():
    while True:
        show_menu()
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
            print("\nThank you for using Contact Management System")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
main()
