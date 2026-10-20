import threading
import time


sq = []
cb = []

def square(s,e,a,name,virsion):
    for i in range(s,e):
        print(a,time.strftime("%H:%M:%S"),":",i*i)
        print(a,time.ctime(),":",i*i)
        print(name,virsion,sep="\t")
        sq.append(i * i)
        time.sleep(1)

def cube(s,e,a,name,virsion):
    for i in range(s,e):
        print(a,time.strftime("%H:%M:%S"),":",i*i*i)
        print(a,time.ctime(),":",i*i*i)
        print(name,virsion,sep="\t")
        cb.append(i * i * i)
        time.sleep(1)

t1 = threading.Thread(target=square,args=(1,11,"square","thread1","v1.0"))
t2 = threading.Thread(target=cube,args=(1,11,"cube","thread2","v1.0"))

t1.start()
t2.start()  

t1.join()
t2.join()

print(sq)
print(cb)