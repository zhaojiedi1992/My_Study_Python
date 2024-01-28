#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import threading 

local_school = threading.local

def process_student():
    stu = local_school.student 
    print("{} {}",threading.current_thread().name,stu)

def process_thread(name):
    local_school.student = name 
    process_student()

t1 = threading.Thread(target=process_thread,args=("zhao",),name="thread-zhao")
t2= threading.Thread(target=process_thread,args=("qian",),name="thread-qian")
t1.start()
t2.start()
t1.join()
t2.join()
