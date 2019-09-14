class Employee:
    # define global object variables
    employee_count = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # defining instance variables
        self.id = Employee.employee_count + 1
        self.first = first.lower()
        self.last = last.lower()
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        self.pay = pay
        # update global object variable with count of instances created
        Employee.employee_count += 1

    def fullname(self):
        # returns the full name of employee
        return '{} {}'.format(self.first.capitalize(), self.last.capitalize())

    def apply_raise(self):
        # applies raise to employee based on the amount in the object global variable
        self.pay = round(int(self.pay) * Employee.raise_amount, 2)
