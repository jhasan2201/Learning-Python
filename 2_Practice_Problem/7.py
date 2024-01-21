def removeDuplicate(items):
    setItem = ()
    itemList = []

    for x in items:
        setItem.add(x)

    # for x in setItem:
    #     itemList.insert(x)

    return setItem

a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

b =  removeDuplicate(a)
print(a)