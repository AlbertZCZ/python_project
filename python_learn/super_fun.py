from functools import reduce

def f(n):
    return n * n

a = list(range(1,11))
print('a = ',a)
b = list(map(f,a))
print('b = ',b)

#把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
    return x * 10 + y

c = reduce(fn,[1, 3, 5, 7, 9])
print('c = ',c)

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    print(digits[s])
    return digits[s]


print(reduce(fn,map(char2num,'13579')))

#把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
#可以接受一个list并利用reduce()求积
def prod(L):
    def f (x,y):
        return x * y
    
    return reduce(f,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')



#filter
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

#sort
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#按名字排序
def by_name(t):
    return t[0]
#再按成绩从高到低排序
def by_score(t):
    return -t[1]

L2 = sorted(L, key=by_score)
print(L2)


#闭包
def createCounter():
    #生成器生成有序数列1，2，3......
    def d():
        n = 0
        while True:
            n += 1
            yield n
    a = d()
    def counter():
        return next(a)
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


#匿名函数
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
L2 = list(filter(lambda x : x % 2 == 1,range(1,20)))
print('L1',L,'L2:',L2)