
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

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if(day.weekday()==5 or day.weekday()==6):
            return False
        return True;


emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)


# REGULAR METHOD

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# CLASS METHOD

# Employee.set_raise_amt(1.05)
# emp_1.set_raise_amt(1.05)
#

# new_emp_1 = Employee.from_string('John-Doe-70000')
#
# print('{} {} {} {}'.format(new_emp_1.first,new_emp_1.last,new_emp_1.email,new_emp_1.pay))
#


# STATIC METHOD

import datetime
my_date = datetime.date(2016,7,11)
print(Employee.is_workday(my_date))


