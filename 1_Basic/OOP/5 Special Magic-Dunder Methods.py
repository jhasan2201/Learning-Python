class Employee:
    num_of_emp = 0
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first + '.' + last + '@gmail.com'

        Employee.num_of_emp += 1

    def fullName(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)

print(emp_1)

# print(repr(emp_1))



