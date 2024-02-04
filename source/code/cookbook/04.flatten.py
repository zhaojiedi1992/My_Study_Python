from collections.abc import Iterable

def flatten(item,ignore_types=(str,bytes)):
    for x in item:
        if isinstance(x,ignore_types):
            yield x
        elif  isinstance(x, Iterable) :
            yield from flatten(x)
        else: 
            yield x 

items = [1, 2, [3, 4, [5, 6], 7], 8,'abc']
print(list(flatten(item=items)))
    