import threading
import time
import  os

def file_read_write(file1,file2):
    os.chdir("D:\\content")

    with open(file1, 'r') as f1:
        mydata=f1.read()
        f1.close()

    with open(file2, 'w') as f2:
        f2.write(mydata)
        f2.close()

    print(time.strftime("%H:%M:%S"),"File copied successfully")

t1=threading.Thread(target=file_read_write,args=("emp.txt","new_emp.txt"))
t1.start()
t1.join()