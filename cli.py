from models import Contact, db


def create_contact():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    Contact.create(
        first_name=first_name, last_name=last_name, phone_number=phone_number
    )
    print("Contact created successfully.")


def list_contacts():
    for contact in Contact.select():
        print(f"{contact.first_name} {contact.last_name} {contact.phone_number}")


def find_contact_by_name():
    first_name = input("Enter first name: ")
    try:
        contact = Contact.get(Contact.first_name == first_name)
        print(f"{contact.first_name} {contact.last_name} {contact.phone_number}")
    except Contact.DoesNotExist:
        print("Contact not found")


def main():
    db.connect()

    while True:
        print("\nContact Book Menu:")
        print("1: Create new contact")
        print("2: List all contacts")
        print("3: Find contact by name")
        print("4: Exit")
        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            create_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            find_contact_by_name()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4")

    db.close()


if __name__ == "__main__":
    main()
