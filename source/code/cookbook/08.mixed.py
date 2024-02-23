class LoggedMappingMixin:
    __slots__ = ()

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {}' .format(key, value))
        return super().__setitem__(key, value)
    
    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)
    
class LoggedDict(LoggedMappingMixin, dict):
    pass

d = LoggedDict()
d['x']=1
print(d['x'])


def LoggedMapping(cls):
    """第二种方式：使用类装饰器"""
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return cls_getitem(self, key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls


@LoggedMapping
class LoggedDictv2(dict):
    pass


d = LoggedDictv2()
d['x'] = 23
print(d['x'])