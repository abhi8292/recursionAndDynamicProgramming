import threading
import time

def doSometing(name,time1):

    for i in range(10):
        print(threading.active_count())
        print(name , " is running")
        time.sleep(time1)


t1 = threading.Thread(target=doSometing,args=('Thread1',1))
t2 = threading.Thread(target=doSometing,args=('Thread2',1))

t1.start()
t2.start()
t1.join(2)
t2.join(2)
print("Execution done")