import math

#绝对值
print(abs(-3))
# 16进制
print(hex(2))
#定义函数
def aren(x):
    return math.pi * x * x

#print(aren(3))

def power(x,n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

#print(power(2,3))

def calc(x):
    sum = 0
    for i in x:
        sum += i
    return sum

print(calc([3,4]))
#可变参数 a，b，c…
def change(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum
#允许你传入0个或任意个含参数名的参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Jack', 24)
person('Jack', 24,hhh=333)
extra = {'city': 'Beijing', 'job': 'Engineer'}
#简写
person('Jack', 24, **extra)
person('Jack', 24, city=extra['city'], job=extra['job'])

L = list(range(100))
print(L[-5:])

def trim(s):
    length = len(s)
    if length > 0:
        begin = 0
        end = length-1
        while s[begin] == ' ' and begin <= length:
            begin += 1
        while s[end] == ' '  and end >= begin:
            end -= 1
        s = s[begin:end+1]
        print(s)
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')