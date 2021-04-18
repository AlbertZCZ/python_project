import time

a = (1,2,3,4,5,6,7,8)

b = 4
c = tuple(filter(lambda i : i <= b,a))
location = len(c)
print('type of c is :',type(c))
print('type of a is :',type(a))
print(c)

print('location:',location)

print(a[location])
num = 5

while num < 10:
    num += 1
    if num == 9:
        continue
    print(num)
    time.sleep(1)