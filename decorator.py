#装饰器

#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time
import functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        begin = time.time()
        ff = fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, time.time() - begin))
        return ff
    
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')