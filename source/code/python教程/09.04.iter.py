#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a 
        if isinstance(n,slice):
            start =n.start 
            stop = n.stop 
            if start is None:
                start =0 
            res = [] 
            a,b=1,1
            for x in range(stop):
                if x>=start:
                    res.append(a)
                
                a,b=b,a+b
            return res 
    

f = Fib()
for i in f:
    print(i)

print(f[1:2])
print(f[:4])