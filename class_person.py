# there is a class where i save information about one person
# each contact have 6 fields with info
class Person:
    def __init__(self, first, last, age, phone_number, working_number, home_phone_number):
        self.first = first
        self.last = last
        self.age = age
        self.phone_number = phone_number
        self.working_number = working_number
        self.home_phone_number = home_phone_number

    def all_numbers(self):
        return f"{self.phone_number} {self.working_number} {self.home_phone_number}"

    def full_name(self):
        return f'{self.first} {self.last}'
    def __str__(self):
        return f"{(self.first)};{self.last};{self.age};{self.phone_number};{self.working_number};{self.home_phone_number}"
