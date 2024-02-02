#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 
from multiprocessing import Process

def f(name):
    print("name")
p = Process(target=f,args=("test",))
print("process start")
p.start()
p.join()
print("process end ")
