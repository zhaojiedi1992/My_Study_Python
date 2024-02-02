#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe_v2(items,key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

if __name__ == "__main__":
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))
    b= [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
    print(list(dedupe_v2(b, key=lambda d: (d['x'],d['y']))))


