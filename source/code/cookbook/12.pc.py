import random
import time 
def producer(q):
    while True:
        q.put(random.randint(0, 1000))
        time.sleep(0.5)

def consumer(q):
    while True:
        print(q.get())
        time.sleep(0.5)

if __name__ == '__main__':
    from queue import Queue
    q = Queue()
    from threading import Thread
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()
    