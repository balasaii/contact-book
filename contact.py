import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bala2002",
    database="phonebook"
)
cursor = con.cursor()

def add_contact(name, phone, email, address):
    sql = "INSERT INTO contacts (name, phone, email, address) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, phone, email, address))
    con.commit()
    print("Contact added successfully!")

def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    for row in cursor.fetchall():
        print(row)

def update_contact(contact_id, name, phone, email, address):
    sql = "UPDATE contacts SET name=%s, phone=%s, email=%s, address=%s WHERE id=%s"
    cursor.execute(sql, (name, phone, email, address, contact_id))
    con.commit()
    print("Contact updated successfully!")

def delete_contact(contact_id):
    sql = "DELETE FROM contacts WHERE id=%s"
    cursor.execute(sql, (contact_id,))
    con.commit()
    print("Contact deleted successfully!")

def menu():
    while True:
        print("\n--- Phone Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            add_contact(name, phone, email, address)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            contact_id = int(input("Enter Contact ID to Update: "))
            name = input("Enter New Name: ")
            phone = input("Enter New Phone: ")
            email = input("Enter New Email: ")
            address = input("Enter New Address: ")
            update_contact(contact_id, name, phone, email, address)

        elif choice == '4':
            contact_id = int(input("Enter Contact ID to Delete: "))
            delete_contact(contact_id)

        elif choice == '5':
            print("Exiting Phone Book...")
            break

        else:
            print("Invalid choice! Please try again.")

menu()

cursor.close()
con.close()
