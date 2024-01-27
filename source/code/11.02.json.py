#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json 

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    


s = Student("zhangsan",16,100)

print(json.dumps(s.__dict__))

def student2dict(student):
    return {
        "name": student.name,
        "age": student.age,
        "score": student.score
    }

print(json.dumps(s,default=student2dict))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
