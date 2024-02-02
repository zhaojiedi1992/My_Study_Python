#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open('./out.log','r',encoding='utf-8',errors='ignore') as f:
    print(f.read())

with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')