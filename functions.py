from file import *
from terminaltables import AsciiTable
from datetime import *
# --------------------------------functions to proof input from user-----------------------------------------
#decorator for wrong input
def decorator_while(func):
    def wrap(string):
        while True:
            string = func(string)
            if string != False:
                return string
            else:
                print("Wrong format.Try again")
                string = input()
    return wrap
# functions return false if data not in right format
#proof number
@decorator_while
def proof_phone_number(number : str) -> bool or str:
    # if user was no telephone
    if number == "":
        return ""
    # if user write home telephone (7 dijits)
    elif len(number) == 7:
        return "8831" + number
    #  if user write number with +7
    elif number[0] == '+' and len(number) == 12:
        return "8" + number[2:]
    # user write a mistake
    elif len(number) != 11:
        return False
    #  if user write number with 7
    else:
        return "8" + number[1:]

# proof name
@decorator_while
def proof_name(name: str) -> bool or str:
    if name:
        name = str.capitalize(name)
        return name
    else:
        return False
#proof age
@decorator_while
def proof_age(age : str) -> bool or str:
    try:
        datetime.strptime(age,"%d.%m.%Y")
        return age
    except ValueError:
        return False
# --------------------------------------------------------------------------------------------------------------
# write table with conctacts in beautiful way
def draw_ackii_table(contacts : list):
    table_data = [['First Name', 'Second Name', 'Date of Birth', 'Phone Number', 'Working Number', 'Home Number']]
    for contact in contacts:
        table_data.append((str(contact).split(';')))
    print(AsciiTable(table_data).table)
#----------------------------functionc for interface---------------------------------------
# function compare users input full name with full names in contacts list
def delete_contact(full_name : str, contacts : list, file_name : str) -> bool:
    for contact in contacts:
        if full_name == contact.full_name():
            #delete from class
            contacts.remove(contact)
            #rewrite file
            rewrite_file(contacts, file_name)
            #if contact was found
            return True
    #if contact was not found
    return False

#function find ane information(number,name,date)
def find_information(info : str, contacts : list) -> bool:
    names, numbers, date, sorted_contacts = [], [], [], []
    # sort input info in 3 arrays
    for s in info.split(" "):
        if s.isdigit():
            numbers.append(s)
        elif "." in s:
            date.append(s)
        else:
            names.append(s)
    # compare info in arrays with contacts class
    for contact in contacts:
        count = 0 # counter for matching
        if names:
            for name in names:
                if proof_name(name) in contact.full_name():
                    count += 1
        if numbers:
            for number in numbers:
                if number in contact.all_numbers():
                    count += 1
        if date and date[0] == contact.age:
            count += 1
        if count == len(names) + len(date) + len(numbers):
            sorted_contacts.append(contact)
    if sorted_contacts:
        draw_ackii_table(sorted_contacts)
        return True
    else:
        return False

#function add contact to adress book
def add_contact(file_name: str, contacts : list):
    print("Enter your contact's information")
    first_name = proof_name(input("First name = "))
    last_name = proof_name(input("Last name = "))
    age = proof_age(input("Date of birth. Format \"%d.%m.%y\" = "))
    phone_number = proof_phone_number(input("Phone number = "))
    working_number = proof_phone_number(input("Working number = "))
    home_number = proof_phone_number(input("Home number = "))
    our_contact = Person(first_name, last_name, age, phone_number, working_number, home_number)
    #proof if contact already exist, return -1 if not
    contact_index = find_contact_in_adress_book(f'{our_contact.first} {our_contact.last}', contacts)

    if contact_index != -1:
        #option to change information about client
        users_input = input('This client already exist. Do you want to change info\n1-Yes 2-No\n')
        if users_input == "1":
            change_info(contacts[contact_index])
            rewrite_file(contacts, file_name)
    else:
        #add contacts if client does not exist
        contacts.append(our_contact)
        if os.path.getsize(file_name):
            rewrite_file(contacts, file_name)
        else:
            update_file(contacts, file_name)

#fucntion compare input full_name with full name in class
#return -1 if contact was not found
def find_contact_in_adress_book(full_name : str, contacts : list) -> int :
    for contact in contacts:
        if full_name == contact.full_name():
            return contacts.index(contact)
    else:
        return -1

#while client do not enter  "q",options to enter new information
def change_info(contact: Person):
    users_input = None
    while users_input != 'q':
        os.system("cls")
        users_input = input('1 - Change name\n'
                            '2 - Change second name\n'
                            '3 - Change age\n'
                            '4 - Change personal phone number\n'
                            '5 - Change working phone number\n'
                            '6 - Change home number\n'
                            'q - exit\n')
        if users_input == '1':
            contact.first = proof_name(input("First name = "))
        elif users_input == "2":
            contact.last = proof_name(input("Last name = "))
        elif users_input == "3":
            contact.age = proof_age(input("Date of birth = "))
        elif users_input == "4":
            contact.phone_number = proof_phone_number(input("Phone number = "))
        elif users_input == "5":
            contact.working_number = proof_phone_number(input("Working number = "))
        elif users_input == "6":
            contact.home_phone_number = proof_phone_number(input("Home number = "))

#calculate age with module date
def contact_age(age: str) -> int:
    today = date.today()
    birth_date = datetime.strptime(age, "%d.%m.%Y")
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# function find clients with birthdays in current month, current today day = real today day
def find_birthday(contacts : list) -> list:
    sorted_contacts = []
    today = date.today()
    for contact in contacts:
        if contact.age != '':
            #receive age client
            new_data = (contact.age).rstrip().split(".")
            #reform info into correct format
            # install current year for right calculating
            d1 = date(today.year, int(new_data[1]), int(new_data[0]), )
            if (today - d1).days <= 30:
                sorted_contacts.append(contact)
    return sorted_contacts


def sort_contacts_by_age(string : str, contacts:list) -> list:
    try:
        operator = string[0]
        years = int(string[1:])
    except:
        return -1
    sorted_contacts = []
    today = date.today()
    for contact in contacts:
        if contact.age != '':
            age = contact_age(contact.age)
            if operator == "<" and age < years:
                sorted_contacts.append(contact)
            elif operator == ">" and age > years:
                sorted_contacts.append(contact)
            elif operator == "=" and age == years:
                sorted_contacts.append(contact)
    return sorted_contacts