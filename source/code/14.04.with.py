#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('start')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    
    def query(self):
        print('Query info about %s...' % self.name)


with Query("abc") as f:
    f.query()



from contextlib import contextmanager

class QueryV2(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = QueryV2(name)
    yield q
    print('End')


with create_query("abc") as q: 
    q.query()



@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

