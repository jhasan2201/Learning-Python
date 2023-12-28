
if True :
    print('Conditional is true')

if False :
    print('Conditional is true')

language = 'Java'

if language=='Python':
    print('Language is Python')
elif language=='Java':
    print('Language is Java')
    print('another language is c++')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

user = 'Admin'
logged_in =True

if user == 'Admin' and logged_in :
    print('Admin page')
else:
    print('Bad creds')

logged_in = False
if user == 'Admin' or logged_in :
    print('Admin page')
else:
    print('Bad creds')

if not logged_in:
    print('Please log in')
else :
    print('Welcome')

a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a is b)

print(id(a))
print(id(b))

b=a
print(a is b)    # id(a) == id(b)

condition = None
if condition:
    print('Evaluation is true')
else:
    print("Evaluation is false")

condition = 0
if condition:
    print('Evaluation is true')
else:
    print("Evaluation is false")

condition = 10
if condition:
    print('Evaluation is true')
else:
    print("Evaluation is false")

condition = []
if condition:
    print('Evaluation is true')
else:
    print("Evaluation is false")

condition = {}
if condition:
    print('Evaluation is true')
else:
    print("Evaluation is false")

condition = 'Jehan'
if condition:
    print('Evaluation is true')
else:
    print("Evaluation is false")

condition = ''
if condition:
    print('Evaluation is true')
else:
    print("Evaluation is false")