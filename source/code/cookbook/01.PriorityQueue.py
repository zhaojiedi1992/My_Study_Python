#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq

class PriorityQueue():
    def __init__(self) -> None:
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
    


if __name__ == "__main__":
    q = PriorityQueue()
    print(q.push(Item('foo'), 1))
    print(q.push(Item('bar'), 5))
    print(q.push(Item('spam'), 4))
    print(q.push(Item('grok'), 1))
    print(q.pop())