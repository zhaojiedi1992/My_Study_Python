#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = 30 

match age :
    case x if x <1: 
        print("婴儿")
    case 10:
        print("age =10 ")
    case 20|21|22:
        print("age >=20 <=22")
    case _:
        print('not sure.')