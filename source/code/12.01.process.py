#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 
print("process {} start ".format(os.getpid()))

pid = os.fork()
if pid ==0 : 
    print("i am child ,my pid={},ppid={}".format(os.getpid(),os.getppid()))
else:
    print("i am parent,my pid {}, my child pid {}".format( os.getpid(),pid))