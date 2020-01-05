from threading import Thread,Lock
import time

# 创建全局变量
g_num = 0

lock = Lock()

def test1():
    # 在函数中引用全局变量
    global g_num
    # 给线程上锁
    lock.acquire()
    for i in range(1000000):
        g_num = g_num + 1

    # 关闭线程锁
    lock.release()
    print("test1---g_num = %d" %g_num)

def test2():
    # 在函数中引用全局变量
    global g_num
    # 给线程上锁
    lock.acquire()
    for i in range(1000000):
        g_num = g_num + 1

    # 关闭线程锁
    lock.release()
    print("test2---g_num = %d" %g_num)

t1 = Thread(target=test1)
t1.start()

t2 = Thread(target=test2)
t2.start()

"""
运行结果是2000000，数据是累加的，如果我们不加线程锁，
两个线程的运算是出现重叠现象，并不是两个线程数据相加，
而是大在小于两者之和。
"""
