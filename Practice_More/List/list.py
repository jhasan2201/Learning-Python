
# 1. Write a Python program to sum all the items in a list.
def sumAllNum(items):
    sum = 0
    for x in items:
        sum += x
    return sum
print(sumAllNum([1, 2, -8]))


# 2. Write a Python program to multiply all the items in a list.
def mulAllNum(items):
    mul = 1
    for x in items:
        mul *= x
    return mul
print(mulAllNum([1, 2, -8]))


# 3. Write a Python program to get the largest number from a list.

def getMax(items):
    return max(items)

print(getMax([1, 2, -8, 0]))

# 4. Write a Python program to get the smallest number from a list.

def getMin(items):
    return min(items)

print(getMin([1, 2, -8, 0]))


# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
def firstLastSame(items):
    count=0
    for x in items:
        if(len(x)>=2 and x[0]==x[-1]):
            count+=1
    return count
print(firstLastSame(['abc', 'xyz', 'aba', '1221']))

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.



# 7. Write a Python program to remove duplicates from a list.
def removeDuplicate(items):
    revDup = []
    setList = set()
    for x in items:
        if x not in setList:
            setList.add(x)
            revDup.append(x)
    return revDup

print(removeDuplicate([10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]))

# 8. Write a Python program to check if a list is empty or not.
def isEmpty(items):
    if not items:
        return True;
    return False

print(isEmpty([]))


# 9. Write a Python program to clone or copy a list.

def cloneList(items):
    newList = items
    return newList

original_list = [10, 22, 44, 23, 4]
print(cloneList(original_list))


# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

def longerThanN(sentence,n):
    words = sentence.split(' ')
    selected = []
    for x in words:
        if len(x) > n:
            selected.append(x)
    return selected

print(longerThanN('The quick brown fox jumps over the lazy dog',3))

# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

def oneCommon(list1,list2):
    for x in list1:
        for y in list2:
            if x==y :
                return True
    return False

print(oneCommon([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

def afterRemoveSome(items):
    items = [x for (i,x) in enumerate(items) if i not in (0,4,5)]
    return items

print(afterRemoveSome( ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

def make3DStar():
    threeD = [[['*' for col in range(6)] for row in range(4)] for matrix in range(3)]
    return threeD

print(make3DStar())

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

def removeEven(items):
    items = [x for x in items if x%2!=0]
    return items

print(removeEven([7, 8, 120, 25, 44, 20, 27]))

# 15. Write a Python program to shuffle and print a specified list.

from random import shuffle
def shuffItems(items):
    shuffle(items)
    return items

print(shuffItems(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

# 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).

def checkPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def checkAllPrime(nums):
    count = 0
    for x in nums:
        if checkPrime(x):
            count+=1
    return len(nums) == count

print(checkAllPrime([3, 5, 7, 13]))

# 18. Write a Python program to generate all permutations of a list in Python.

import itertools

print(list(itertools.permutations[1,2,3]))

# 19. Write a Python program to calculate the difference between the two lists.

def diffOfList(list1,list2):
    set1 = list(set(list1) - set(list2));
    set2 = list(set(list2) - set(list1));
    return set1 + set2

print(diffOfList([1, 3, 5, 7, 9],[1, 2, 4, 6, 7, 8]))


# 20. Write a Python program to access the index of a list.
def indexAndVal(items):
    for i,x in enumerate(items):
        print(f'{i} {x}')


indexAndVal([5, 15, 35, 8, 98])


# 21. Write a Python program to convert a list of characters into a string.
def joinIn(items):
    str = ''.join(items)
    return str

print(joinIn(['a', 'b', 'c', 'd']))

# 22. Write a Python program to find the index of an item in a specified list.

def findIndex(items,key):
    return items.index(key)

print(findIndex([10, 30, 4, -6],30))


# 25. Write a Python program to select an item randomly from a list.

import  random
def randomSelection(items):
    return random.choice(items)

print(randomSelection(['Red', 'Blue', 'Green', 'White', 'Black']))

# 27. Write a Python program to find the second smallest number in a list.

def findSecSmall(items):
    setItem = set()
    listItem = []
    for x in items:
        if x not in setItem:
            setItem.add(x)
            listItem.append(x)

    if len(listItem)>=2:
        listItem.sort()
        return listItem[1]
    return


print(findSecSmall([2, 2]))

# 28. Write a Python program to find the second largest number in a list.
def findSeclarge(items):
    setItem = set()
    listItem = []
    for x in items:
        if x not in setItem:
            setItem.add(x)
            listItem.append(x)

    if len(listItem)>=2:
        listItem.sort(reverse=True)
        return listItem[1]
    return


print(findSeclarge([1, 1, 1, 0, 0, 0, 2, -2, -2]))


# 29. Write a Python program to get unique values from a list.
def getUnique(items):
    setItem = set(items)
    items = list(setItem)
    return items

print(getUnique([10, 20, 30, 40, 20, 50, 60, 40]))

# 30. Write a Python program to get the frequency of elements in a list.

from collections import Counter
def freqCount(items):
    return Counter(items)

print(freqCount([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]))

# using dictionary

def freqCount2(items):
    frq = {}
    for x in items:
        frq[x] = 0
    for x in items:
        frq[x] += 1
    return frq
print(freqCount2([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]))





