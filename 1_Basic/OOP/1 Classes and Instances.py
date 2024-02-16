
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first + '.' + last + '@gmail.com'

    def fullName(self):
        return '{} {}'.format(self.first,self.last)



emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)


print(emp_1.fullName())
print(emp_2.fullName())

print(Employee.fullName(emp_1))


# print('{} {}'.format(emp_1.first,emp_1.last))

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'cschafer@gmail.com'
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'testuser@gmail.com'
# emp_2.pay = 60000
#
# print(emp_1.email)
# print(emp_2.email)
