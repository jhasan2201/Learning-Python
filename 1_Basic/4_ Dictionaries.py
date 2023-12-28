
student = {'name':'John','age':25,'courses':['Math','CompSci'],1:'Jehan'}

print(student)
print(student['name'])
print(student['courses'])
print(student[1])
# print(student['Phone'])
print(student.get('Phone'))
print(student.get('Phone','Not found'))

student['Phone'] = '555-5555'
print(student.get('Phone'))

student['name'] = 'Jane'
print(student)

student.update({'age': 26, 'Phone':'555-5556'})
print(student)

student['height'] = 5.9
print(student)

age = student.pop('age')
print(age)

del student['Phone']

print(student)

print(len(student))

print(student.keys())
print(student.items())

for key in student:
    print(key)

for key,value in student.items():
    print(key, value)



