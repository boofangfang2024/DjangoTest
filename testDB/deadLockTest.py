from threading import Lock,Thread
import time

def test1():
    #lock1上锁
    if lock1.acquire():
        print("----do1 --up")
        time.sleep(1)
        #判断lock2是否能上锁,此时lock2锁并没有解锁，需要等到lock2解锁才能上锁

        if lock2.acquire():
            print("----do2 ---up")
        #lock1解锁
        lock1.release()


def test2():
    #lock2上锁
    if lock2.acquire():
        print("----do2 --up")
        time.sleep(1)

        #判断lock1是否能上锁,此时lock2锁并没有解锁，需要等到lock1解锁才能上锁
        if lock1.acquire():
            print("----do1 ---up")
        #lock2解锁
        lock2.release()

'''
        test1中的lock1在等待test2中lock2解锁才能对lock2上锁，而test2中lock2需要test1中的lock1解锁
        才能对lokc1上锁，此时test1中的lock2在等test2中的lock2解锁， 而test2的lock1在等test1中的lock1解 
        锁，两者程序在这卡住，无法进行下去，此时叫死锁
'''

#创建两把锁
lock1 = Lock()

lock2 = Lock()

#创建线程实例
t1 = Thread(target= test1)

t2 = Thread(target= test2)
#执行线程
t1.start()
t2.start()