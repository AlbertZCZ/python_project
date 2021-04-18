from collections.abc import Iterable

print(isinstance('abc',Iterable))

test_dict = {'a':1,'b':3,'c':4}
for k,v in test_dict.items():
    print(k)
    print(v)


def findMinAndMax(L):
    if type(L) != list or len(L) == 0:
        return (None, None)

    min = L[0]
    max = L[0]
    for item in L:
        if item < min:
            min = item
        if item > max:
            max = item
    return(min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')