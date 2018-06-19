


#Q1


import threading
import time

class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        time.sleep(5)
        print("value send",self.h)
thread1=mythread(1)
thread1.start()


#Q2



import threading
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i+1
    def run(self):
        print(self.h)

for i in range(10):
    thread1=mythread(i)
    thread1.start()
    time.sleep(1)



#Q3




import threading
import time
l=[2,4,6,8,10]
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self,counter):
        time.sleep(counter)
        print(self.h)

for i in l:
    thread=Mythread(i)
    thread.run(i)



#Q4



import threading
import math
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        a=self.h
        b=math.factorial(a)
        print("factorial is =",b)
n=int(input("enter number to get factorial"))
thread=Mythread(n)
thread.start()
