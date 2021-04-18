class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        if isinstance(n,int):
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[3])
print(f[1:5])