#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print(f.status)
    print(data)

# todo post 