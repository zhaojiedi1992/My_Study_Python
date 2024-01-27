#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def study(self,book):
        print(f"study {book}")

def study_v2(self,book):
    print(f"study {book}")

StudentV2 = type('StudentV2',(object,),dict(study_v2=study_v2))

s = StudentV2()
s.study_v2("math")