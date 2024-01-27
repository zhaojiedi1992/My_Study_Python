#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal():
    pass 

class Flyable():
    def fly(self):
        print("fly")
class Bid(Animal,Flyable):
    pass

