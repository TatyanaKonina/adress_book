from functions import *


def app(contacts : list):
    file_name = "contacts.csv"
    open_file(contacts, file_name)
    users_input = ""
    print("Welcome to the address book program")
    while users_input != "q":
        os.system("cls")
        print("Available options")
        print("1 - Enter a contact")
        print("2 - Display contacts")
        print("3 - Find contact")
        print("4 - Delete contact")
        print("5 - Change contact info")
        print("6 - Display contact age")
        print("7 - Display current birthdays")
        print("8 - Display older / younger / exactly than N years old")
        print("q - quit program")
        users_input = input("Select option: ")
        # time.sleep(1)
        os.system("cls")
        if users_input == "1":
            add_contact(file_name, contacts)
            print("Thank you we have received your contacts information")
            input("Hit enter to continue.")
        elif users_input == "2":
            if contacts:
                draw_ackii_table(contacts)
                print("Contacts displayed")
            else:
                print("Our book is empty")
            input("Hit enter to continue.")
        elif users_input == "3":
            to_lookup = input("Enter information to lookup: ")
            if find_information(to_lookup, contacts):
                input("Information was found.Hit enter to continue.")
            else:
                print("Sorry, no information")
        elif users_input == "4":
            full_name = input("Please write full name of the contact: ")
            full_name = ' '.join([proof_name(x) for x in full_name.split(" ")])
            if delete_contact(full_name, contacts, file_name):
                print("Contact was deleted")
            else:
                print('Contact was not found')
            input("Hit enter to continue.")
        elif users_input == "5":
            draw_ackii_table(contacts)
            full_name = input("Please write full name of contact that you want to change:")
            full_name = ' '.join([proof_name(x) for x in full_name.split(" ")])
            contact_index = find_contact_in_adress_book(full_name, contacts)
            if contact_index != "-1":
                change_info(contacts[contact_index])
                rewrite_file(contacts, file_name)
            else:
                print('You made a mistake. Contact does not exist')
            input("Hit enter to continue.")
        elif users_input == "6":
            draw_ackii_table(contacts)
            full_name = input("Please write full name of contact that you want to change:")
            full_name = ' '.join([proof_name(x) for x in full_name.split(" ")])
            contact_index = find_contact_in_adress_book(full_name, contacts)
            if contact_index == -1:
                print('You made a mistake. Contact does not exist')
            else:
                print(f"{contacts[contact_index].full_name()} age is {contact_age(contacts[contact_index].age)}")
            input("Hit enter to continue.")
        elif users_input == "7":
            sorted_contacts = find_birthday(contacts)
            if sorted_contacts:
                print("Here the list of birthdays:")
                draw_ackii_table(sorted_contacts)
            else:
                print('No birthdays!!!')
            input("Hit enter to continue.")
        elif users_input == '8':
            sorted_contacts = sort_contacts_by_age(input(
                "Write in format: \">\"- older\\\"<\"- younger\\\"=\"- exactly N years old. Example(\">60\")"), contacts)
            if sorted_contacts == -1:
                print("Wrong input!!!")
            elif sorted_contacts:
                draw_ackii_table(sorted_contacts)
            else:
                print('I can not find any person!!!')
            input("Hit enter to continue.")
        elif users_input.lower() == "q":
            break
    print("Thank you for using the address book")

if __name__ == "__main__":
    contacts = list()
    app(contacts)
