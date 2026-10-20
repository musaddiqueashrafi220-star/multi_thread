import time
import threading

def display():
    l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for i in l1:
        print(i)
        time.sleep(1)

def sum():
    l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    total=0
    for i in l1:
        total+=i
        print("sum is",total)
        time.sleep(1)

t1 = threading.Thread(target=display)
t2 = threading.Thread(target=sum)

t1.start()
t2.start()

t1.join()
t2.join()