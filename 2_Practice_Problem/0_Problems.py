
#-------> 1. Write a Python program to sum all the items in a list.

# print(sum([4,5,6,9]))


#-------> 2. Write a Python program to multiply all the items in a list.

# nums = [4,5,-2]
# def mul(nums):
#     sum=0
#     for x in nums:
#         sum+=x
#     return sum
#
# print(mul(nums))


#-------> 3. Write a Python program to get the largest number from a list.

# print(max([4,5,-2]))

#-------> 4. Write a Python program to get the smallest number from a list.

# print(min([4,5,-2]))


#------->  5.Write a Python program to count the number of strings from a given list of strings

# def countString(stringList):
#     count=0
#     for x in stringList:
#         if len(x)>2 and x[0]==x[-1]:
#             count+=1
#     return count
#
# print(countString(['abc', 'xyz', 'aba', '1221']))

#-------> 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

def getLast(i):
    return i[-1]

def getfirst(i):
    return i[0]

def sortedLast(items):
    return sorted(items,key=getfirst)

items=  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sortedLast(items))