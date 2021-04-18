#要创建一个generator
g = (x * x for x in range(10))
#print(next(g))
for i in g:
    print(i)

#斐波拉契数列
def feb(max):
    n,a,b, = 0,0,1
    while n < max:
        n += 1
        print(b)
        #a, b = b, a + b
        t = (b, a + b) # t是一个tuple
        a = t[0]
        b = t[1]
    return 'done'

feb(6)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
for i in o:
    print(i)



#杨辉三角
def triangles():
    a = [1]
    while True:
        yield(a)
        a=[sum(i) for i in zip([0]+a,a+[0])]

    pass

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')