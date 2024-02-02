#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass 
class Pig(Animal):
    pass 

dog = Dog()
dog.run()


class Dog2(Animal):
    def run(self):
        print('Dog2 is running...')
class Pig2(Animal):
    def run(self):
        print('Pig2 is running...')


def do_run(animal):
    if not isinstance(animal,Animal):
        return 
    animal.run()

a = Animal()
dog2 = Dog2()
pig2 = Pig2()
do_run(a)
do_run(dog2)
do_run(pig2)
dog2.run()
pig2.run()
