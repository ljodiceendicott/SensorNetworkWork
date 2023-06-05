import threading
from threading import Lock
ct = 0

def do_work(my_arg):
    global ct
    lock = Lock()
    lock.acquire()
    ct = ct + 1
    lock.release()

def main():
    
    for i in range(0,10): 
        th = threading.Thread(target=do_work, args=(None,)) 
        th.start()
    
    while(ct < 10):
        print("waiting...")
    print("All done!")

if __name__ == "__main__":
    main()