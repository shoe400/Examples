# Tyler Tscheulin SDEV 140, 3-3-2022
# Program is to store data, and then ask for user input.
# Version 0.1
# setting up the classes and the main function to call.

class Employee:
    def __init__(self, name, employee_number):
        self.name = name

        self.employee_number = employee_number


class Production_worker(Employee):  # Needs to make an object
    def __init__(self, name, employee_number, shift_number, pay):
        Employee.__init__(self, name, employee_number)

        self.shift_number = shift_number

        self.pay = pay


def main():  # main code where I will get the information from.
    worker_name = input("Enter Your name: ")
    worker_id = input("Enter the ID: ")
    worker_shift = float(input("Enter the shift number: "))
    worker_pay = float(input("Enter the pay rate: "))

    worker = Production_worker(worker_name, worker_id, worker_shift, worker_pay)
    print("Production worker Info:")
    print("Name: ", worker.name)
    print("ID Number: ", worker.employee_number)
    print("Shift: ", worker.shift_number)
    print("Hourly Rate: ", worker.pay)


main()
