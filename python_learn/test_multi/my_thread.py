import threading
lock = threading.Lock()
#多线程数据安全问题
balance = 0

def chang_id(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(2000000):
        # 先要获取锁:
        lock.acquire()
        try:
            chang_id(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

t1 = threading.Thread(target=run_thread,args=(2,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('balance = ',balance)