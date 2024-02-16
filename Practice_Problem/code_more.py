# 1

import random
def sum_list(items):
    x = sum(items)
    return x


print(sum_list([1, 2, -8]))


# 2

def mul_list(items):
    sum = 1
    for x in items:
        sum *= x
    return sum


print(mul_list([1, 2, -8]))


# 3
def findMax(items):
    maxi = max(items)
    return maxi


print(findMax([8, -5, 22, -3]))


# 4
def finMin(items):
    mini = min(items)
    return mini


print(finMin([8, -3, 22, 12]))


# 5
def firstLastMatch(items):
    count = 0
    for x in items:
        if (x[0] == x[-1]):
            count += 1
    return count


print(firstLastMatch(['abc', 'xyz', 'aba', '1221']))


# 6

def lastEle(n):
    return n[-1]


def increasingMake(tupleList):
    return sorted(tupleList, key=lastEle)


print(increasingMake([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# 7
def removeDuplicate(items):
    setList = set()
    for x in items:
        setList.add(x)
    return setList;


print(list(removeDuplicate([10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40])))


# 8
def isEmpty(items):
    if not items:
        return 'List is empty'
    return "Not empty"


print(isEmpty([]))


# 9
def cloneList(items):
    x = items
    return x


oldList = [10, 22, 44, 23, 40]
newList = cloneList(oldList)
print(newList)


# 10
def longerThanN(str, n):
    items = str.split(' ')
    selected = []
    for x in items:
        if (len(x) > n):
            selected.append(x)
    return selected;


print(longerThanN("The quick brown fox jumps over the lazy dog", 3))


# 11
def findCommon(list1, list2):
    for x in list1:
        for y in list2:
            if (x == y):
                return True;
    return False;


print(findCommon([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(findCommon([1, 2, 3, 4, 5], [6, 7, 8, 9]))


# 12
def selectSome(list1):
    list1 = [x for (i, x) in enumerate(list1) if i not in (0, 4, 5)]
    return list1


print(selectSome(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))


def selectSome2(list1):
    list2 = []
    for (i, x) in enumerate(list1):
        if i not in (0, 4, 5):
            list2.append(x)
    return list2;


print(selectSome2(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))


# 13

# 14
def removeOddNumber(nums):
    nums = [x for x in nums if (x % 2 == 0)]
    return nums


print(removeOddNumber([7, 8, 120, 25, 44, 20, 27]))

# 15
from random import shuffle


def suffleList(listItem):
    shuffle(listItem)
    return listItem


print(suffleList(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))


# 16
def genSqList():
    createList = []
    for i in range(1, 21):
        createList.append(i ** 2)
    print(createList[:5])
    print(createList[-5:])


genSqList()


# 17:
def checkPrime(listNum):
   for x in listNum:
       if x == 1:
           return False
       for i in range(2, x):
           if x % i == 0: return False;
   return True


print(checkPrime([0, 3, 4, 7, 9]))
print(checkPrime([3, 5, 7, 13]))
print(checkPrime([1, 5, 3]))

# 18

import itertools

print(list(itertools.permutations([1,2,3])))

# 19

def diffbetweenList(list1,list2):
    unionSet = set(list1).union(set(list2))
    interSet = set(list1).intersection(set(list2))
    return list(unionSet - interSet)

print(diffbetweenList([1, 3, 5, 7, 9],[1, 2, 4, 6, 7, 8]))


def diffbetweenList2(list1,list2):
    listDeflist1 = list(set(list1) - set(list2))
    listDeflist2 = list(set(list2) - set(list1))
    return listDeflist1  + listDeflist2;

print(diffbetweenList2([1, 3, 5, 7, 9],[1, 2, 4, 6, 7, 8]))

# 21

def joinIntoString(listchar):
    str = ''.join(listchar)
    return str

print(joinIntoString(['a', 'b', 'c', 'd']))

# 22

arr = [5,8,9,23,8,45,9,7]

print(arr.index(8))  # linear search
arr.append(100)
print(arr)
arr.insert(0,99)
print(arr)

arr.pop(3)
print(arr)

arr.remove(45)
print(arr)

# 24

list1 = [1,2,3,0]
list2 = ['Red','Green','Black']

finalList = list1 + list2
print(finalList)

# 25

import random
print(random.choice(['Red','Green','Black','Yellow','Grey']))

# 26

# 27

def secondSmallesst(itemList):
    if len(itemList)<2:
        return
    if len(itemList)==2  and itemList==itemList[1]:
        return

    setList = set()
    setList = itemList[:]

    setList.sort()
    return setList[1]

print(secondSmallesst([1, 2, -8, -2, 0, -2]))

# 28

def secondLargestesst(itemList):
    if len(itemList)<2:
        return
    if len(itemList)==2  and itemList==itemList[1]:
        return

    setList = set()
    setList = itemList[:]

    setList.sort()
    return setList[-2]

print(secondLargestesst([1, 2, -8, -2, 0, -2]))

# 30

import collections
def countFrequency(itemList):
    ctr = collections.Counter(itemList)
    return ctr

print(countFrequency([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]))

# 30 (dictionary)

def countFreq(itemList):
    disc = {}
    for x in itemList:
        if(x in disc):
            disc[x] += 1
        else:
            disc[x] = 1
    return disc
print(countFreq([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]))

# 31

def countFrqInRange(itemList,min,max):
    count = 0
    for x in itemList:
        if x<=max and x>=min:
            count += 1
    return count

print(countFrqInRange([10, 20, 30, 40, 40, 40, 70, 80, 99],40,100))

# 35

def concatList(itemList,n):
    return ['{}{}'.format(x,y) for x in itemList for y in range(1,n+1)]
print(concatList(['p', 'q'],4))


# 37

def commonItem(itemList1,itemList2):
    return itemList1 & itemList2
print(commonItem({"Red", "Green", "Orange", "White"},{"Black", "Green", "White", "Pink"}))


#  38

def swap(i,j,arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def flipFlop(listItem):
    for i in range(len(listItem)-1):
        swap(i,i+1,listItem)
        i+=2
    return listItem

print(flipFlop([0, 1, 2, 3, 4, 5]))

#  Another

from itertools import zip_longest,chain

def chainThem(listItems):

    return list(chain.from_iterable(zip_longest(listItems[1::2],listItems[::2])))

print(chainThem([0, 1, 2, 3, 4, 5]))

# 39
def listToInt(itemList):
    return int(''.join(map(str,itemList)))
print(listToInt([11, 33, 50]))

def makeDictionary(word_list):
    dictio = {}
    for word in word_list:
        dictio[word[0]]
    return dictio

print(makeDictionary(['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']))

