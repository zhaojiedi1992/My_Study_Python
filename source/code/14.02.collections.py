#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# [namedtuple_start] 
from collections import namedtuple

Point  = namedtuple('Point',['x','y'])
p  = Point(1,2)
print(p.x)
print(p.y)
# [namedtuple_end] 

# [deque_start] 
from collections import deque

q = deque(['a','b','c'])
q.append('d')
q.appendleft('y')
print(q)
# [deque_end] 

# [defaultdict_start]
from collections import defaultdict 

dd = defaultdict(lambda: 'N/A')
print(dd["k1"])
# [defaultdict_end]

# [OrderedDict_start]
from collections import OrderedDict
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d)
# [OrderedDict_end]

# [ChainMap_start]

from collections import ChainMap 
import os 

d1 = { 
    'color': 'red',
    'user': 'zhaojiedi'
}
d2 = {
      'color': 'blue'
}
d3 = {
      'age': 1,
}

combined = ChainMap(d1,d2,d3)
print(combined['color'])
print(combined['age'])
# [ChainMap_end]

# [Counter_start]

from collections import Counter 
c =Counter() 
c.update('hello')
print(c)

# [Counter_end]