import time
import threading

def test():
    print("---这是一个线程---")
    time.sleep(1)

for i in range(5):
    """创建五个线程"""
    t = threading.Thread(target=test) #创建一个线程实例，参数为函数名
    t.start() #开始进入test执行函数

#创建线程类，并继承Thread类
class MyThread(threading.Thread):
    '''子线程创建多任务'''
    def run(self):
        for i in range(6):
            '''创建6个线程'''
            time.sleep(1)
            msg = "I'm" + self.name + "@" + str(i)
            print(msg)
if __name__ == '__main__':
    #创建线程的实例对象
    t = MyThread()
    #调用父类的start对象
    t.start()
    t.join()
