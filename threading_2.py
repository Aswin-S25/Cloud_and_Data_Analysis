import threading
import os

def task1():
    print("Task assigned to the thread 1 : {}".format(threading.current_thread().name))
    print("ID of process runnint taks1 : {}".format(threading.get_ident()))
    
def task2() :
    print("Task assigned to the thread 2: {}".format(threading.current_thread().name))
    print("Process ID of the process runnning task 2 is {}".format(threading.get_ident()))
    
if __name__ == "__main__":
    print("Id of the process running the main program : {}".format(os.getpid()))
    print("main thread name: {}".format(threading.current_thread().name))
    
    t1 = threading.Thread(target=task1, name="t1")
    t2 = threading.Thread(target=task2, name="t2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()