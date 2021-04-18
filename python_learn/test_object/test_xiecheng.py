#协程

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print("[CONSUMER] Consuming... %s" % n)
        r = '200 OK'


def product(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCT] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCT] Consumer return : %s' % r)
    c.close()

c = consumer()
product(c)