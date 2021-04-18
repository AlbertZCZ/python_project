import os

a = [x * x for x in range(1,11) if x % 2 != 0]
print(a)

#双层循环 全排列
b = [m + n for m in 'ABC' for n in 'XYZ']
print(b)

#列出当前目录下的所有文件和目录名
c = [d for d in os.listdir('.')]
print(c)

#最后把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
L = [s.lower() for s in L]
print(L)

#练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')