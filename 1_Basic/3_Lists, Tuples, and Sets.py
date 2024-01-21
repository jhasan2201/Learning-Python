
courses = ['History','Math','Physics','CompSci']
print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

courses.append('Art')
print(courses)

courses.insert(0,'Chemistry')
print(courses)

couses_2 = ['Art','Education']
courses.insert(0,couses_2)
print(courses)
print(courses[0])
print(courses[1:])

courses = ['History','Math','Physics','CompSci']
courses.extend(couses_2)
print(courses)

courses.remove('Math')
print(courses)
popped = courses.pop()
print(courses)
print(popped)

courses.reverse()
print(courses)

nums = [1,5,2,4,3]

courses.sort()
nums.sort()

print(courses)
print(nums)

courses.sort(reverse=True)
nums.sort(reverse=True)

print(courses)
print(nums)

courses = sorted(courses)
print(courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('Physics'))
# print(courses.index('Artt'))

# print('Math' in courses)
# print('Art' in courses)
#
for item in courses:
    print(item)

for index,course in enumerate(courses):
    print(index,course)

for i,x in enumerate(courses):
    print(i,x)

print()
for index, course in enumerate(courses,start=1):
    print(index, course)

course_str = ', '.join(courses)
print(course_str)

course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)


# -------------------------------------------------

tuple_1 = ('Art', 'CompSci', 'History', 'Physics')
tuple_2 = tuple_1

# tuple_1[0] = 'Artt'

print(tuple_1)
print(tuple_1)

cs_course = {'History', 'Physics','DLD','TOC','Physics','Math'}
art_course = {'History','Design','Math'}

print(cs_course)
print('Physics' in cs_course)

print(cs_course.intersection(art_course))
print(cs_course.difference(art_course))
print(cs_course.union(art_course))

#list---------
empty_list = []
empty_list = list()

#tuple -----------
# empty_tuple = ()
# empty_tuple = tuple()


#set------------
# # this is invalid(this is dictionary) :: empty-set = {}
# empty_set = set()
#
#
#
#
