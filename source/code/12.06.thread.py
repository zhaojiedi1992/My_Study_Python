#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time 
import threading
import multiprocessing


balance =0 
lock = threading.Lock()

def change_balance(n): 
    global balance 
    balance = balance + n 
    balance = balance - n 

def run_thread(n): 
    for i in range(20000000 * multiprocessing.cpu_count()):
         lock.acquire()
         try: 
            change_balance(i )
         finally: 
             lock.release()


t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(58,))
t3  = threading.Thread(target=run_thread,args=(58,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join() 
t3.join()

print(balance)