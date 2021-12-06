#count how many
zork = 0
print('before', zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + thing
    print(thing, zork)
print('after', zork)
#total
zork = 0
print('Before', zork)
numbers = [9, 41, 12, 3, 74, 15] # 강의와는 달리 numbers라는 int를 원소로 가지는 list를 선언하였습니다.
for thing in numbers :
    zork = zork + thing
    print(zork, thing)
print('After', zork)
#average
count = 0 # 평균을 전체 원소의 수로 나누기 위해 total number를 확인합니다.
sum = 0
print('Before', count, sum)
numbers = [9, 41, 12, 3, 74, 15] # 강의와는 달리 numbers라는 int를 원소로 가지는 list를 선언하였습니다.
for value in numbers :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)
#filtering #find the biggest num
print('Before')
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers :
    if value > 20:
        print('Large number', value)
print('After')
#search specific value by using boolean
print('Before')
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers :
    if value > 20:
        print('Large number', value)
print('After')
#find the smallest value
largest_so_far = -1
print('before', largest_so_far)
for num in [9,41,12,3,74,15]:
    if num > largest_so_far:
        largest_so_far= num
    print(largest_so_far, num)
print('after', largest_so_far)
#figure out the smallest num
smallest = None
print('Before')
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)



