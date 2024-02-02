#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 
from multiprocessing import Process,Pool
import time 
import random 

def my_task(name):
    time.sleep(random.random()*3)
    print(f"{name} end")

p = Pool(3)
for i in range(5):
    p.apply_async(my_task,args=(i,))
p.close()
p.join()
print("all done")