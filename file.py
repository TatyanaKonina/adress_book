# functions to work with file contacts.csv

import os

from class_person import Person

#function open file and return list of contacts
def open_file(contacts : list, file_name:str):
    if os.path.isfile(file_name):
        with open(file_name) as f:
            csv_list = f.readlines()
            csv_list.pop(0)
            for contact_line in csv_list:
                # each string in file if format "info;info;info..."
                contact_data = contact_line.rstrip().split(";")
                # form conctact
                contact = Person(contact_data[0],
                                 contact_data[1],
                                 contact_data[2],
                                 contact_data[3],
                                 contact_data[4],
                                 contact_data[5])
                contacts.append(contact)
  # return list of class Persons
    return contacts

# function only add new line
def update_file(contacts : list, file_name : str):
    if os.path.isfile(file_name):
        with open(file_name, 'a') as f:
            f.write(f'{contacts[-1]}\n')


#function rewrite file
def rewrite_file(contacts : list, file_name : str):
    if os.path.isfile(file_name):
        with open(file_name, 'w') as f:
            f.write(f'First name;Last Name;Date of birth;Personal number;Working number;Home number\n')
            for contact in contacts:
                f.write(f'{str(contact)}\n')