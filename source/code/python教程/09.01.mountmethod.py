#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self,name) -> None:
        self.name = name 
        pass

s = Student("zhang")
print(s.name)

def set_age(self,age):
    self.age = age 

from types import MethodType

# 给特定实例绑定方法
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

def set_age2(self,age):
    self.age = age 
Student.set_age2 = set_age2







