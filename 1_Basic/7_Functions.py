
def hello_func():
    print('Hello Funtion')

hello_func()

def hello_func2():
    return 'Hello Funtion2'

print(hello_func2())
print(hello_func2().upper())

def hello_print3(greeting):
    return '{} Function.'.format(greeting)

print(hello_print3('Hi'))

def hello_print4(greeting,name='You'):
    return '{} {} Function.'.format(greeting,name)

print(hello_print4('Hi'))
print(hello_print4('Hi','Jehan'))

def student_Info(*args, **kwargs):
    print(args)
    print(kwargs)

student_Info('Math','Art',name='Jehan',age=22)

courses = ['Math','Art']
info = {'name':'Jehan','age':22}
student_Info(courses,info)
student_Info(*courses,**info)

month_days =[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year%4==0 and (year%100!=0 or year%400==0)

def days_in_month(year,month):
    if not 1<= month <=12:
        return 'Invalid month'
    if month==2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2017))
print(days_in_month(2028,2))