#solution to question number 1

import time
import threading
from threading import Thread
def fun1():
     print("bye i m going to sleep")
     time.sleep(5)
     print("hello i m awake")
thread=Thread(target=fun1(),args=())
thread.start()

#solution to question number 2

import time
import threading
from threading import Thread
def printing(i):
    print(i)
    time.sleep(1)
for i in range(11):
    thread = Thread(target=printing(i), args=(i))
    thread.start()

#solution to question number 3

import time
import threading
from threading import Thread
def process():
    list1 = ['s', 'm', 'i', 'l', 'e']
    for i in list1:
        print(i)
        time.sleep(2**2)
thread=Thread(target=process(),args=())
thread.start()


#solution to question number 4

import time
import threading
from threading import Thread
def factorial():
    n = int(input("Enter number:"))
    fact = 1
    while (n > 0):
        fact = fact * n
        n = n - 1
    print("Factorial of the number is: ")
    print(fact)
thread=Thread(target=factorial(),args=())
thread.start()
