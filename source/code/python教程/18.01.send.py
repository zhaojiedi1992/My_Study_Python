#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    for n in range(5): 
        print(f'[PRODUCER] Producing {n}')
        r = c.send(n)
        print(f'[PRODUCER] Consumer return: {r}')
    c.close()

c = consumer()
produce(c)
