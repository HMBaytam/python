class Employee:
    employee_count = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.id = Employee.employee_count + 1
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        self.pay = pay

        Employee.employee_count += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = round(int(self.pay) * Employee.raise_amount, 2)
