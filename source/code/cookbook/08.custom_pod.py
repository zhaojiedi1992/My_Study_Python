import collections
collections.Iterable = collections.abc.Iterable
class A(collections.Iterable):
    def __iter__(self):
        yield 1
    pass


a=A()