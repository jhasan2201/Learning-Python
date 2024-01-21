# import myModule as mm

# from myModule import *

import sys
sys.path.append('C:\Users\HP TECHNOLOGY\Desktop')

from myModule import find_index as fi,test


courses = ['History','Math','Physics',"CompSci"]

# index = mm.find_index(courses,"Math")

# index = find_index(courses,'Math')
index = fi(courses,'Math')
# print(index)
print(test)

print(sys.path)

