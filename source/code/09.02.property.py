#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self,name) -> None:
        self._name = name 
        pass
    def get_age(self):
        return self._age 
    def set_age(self,age):
        if not isinstance(age,int):
            return ValueError("should be int")
        if age <0 or age >200:
            return ValueError("age >=0 && age <=200")
        self._age =age 


class StudentV2(object):
    def __init__(self,name) -> None:
        self._name = name 
        pass
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        if not isinstance(age,int):
            return ValueError("should be int")
        if age <0 or age >200:
            return ValueError("age >=0 && age <=200")
        self._age =age 






