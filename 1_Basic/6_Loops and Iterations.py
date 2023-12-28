
nums = [1,2,3,4,5]

for num in nums:
    if num==3:
        print('\n Found')
        break
    print(num ,end=' ')

print('\nNew loop:')
for num in nums:
    if num==3:
        print('\n Found')
        continue
    print(num,end=' ')

print('\nNew loop:')
for num in nums:
    for letter in 'abc':
        print(num,letter)


print('\nNew loop:')
for i in range(10):
    print(i,end=' ')

print('\nNew loop:')
for i in range(1,11):
    print(i,end=' ')

print('\nNew loop:')
x=0
while True:
    if x==5:
        break
    print(x,end=' ')
    x+=1

