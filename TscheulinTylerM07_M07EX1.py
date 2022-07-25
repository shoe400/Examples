# Tyler Tscheulin SDEV 140, 3-3-2022
# Program is simple it gets information about the customer and prints it back out
# Version 0.1
# Version 0.1 is setting the classes and printing them out.

class Person:  # Class for the person and their info

    def __init__(self, name, address, phone):
        self.name = name

        self.address = address

        self.phone = phone


class Customer(Person):  # Class for the customer which will call the Parent Class of Person.

    def __init__(self, name, address, phone, customer_number, onMail):
        Person.__init__(self, name, address, phone)

        self.customer_number = customer_number

        self.onMail = onMail


def main():  # the main code where I will get the person's info.
    person_name = input("Enter The Name: ")
    person_address = input("Enter The Address: ")
    person_phone = input("Enter The Phone: ")
    person_number = input("Enter The Customer Number: ")
    person_mail = input("Enter on Mail: ")  # How to force a true or false

    person = Customer(person_name, person_address, person_phone, person_number, person_mail)

    print("Customer Info: ")
    print("Name: ", person.name)
    print("Address: ", person.address)
    print("Phone: ", person.phone)
    print("Customer Number: ", person.customer_number)
    print("Mail List: ", person.onMail)


main()
