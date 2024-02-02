#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from multiprocessing import Process, Queue
import os, time, random

def write(q): 
    for value in ['a','b','c']: 
        q.put(value)
        time.sleep(random.random())

def read(q): 
    while True: 
        value = q.get(True)
        print(value)

q = Queue()
pw = Process(target=write,args=(q,))
pr = Process(target=read,args=(q,))

pw.start()
pr.start()
pw.join()
pr.terminate()