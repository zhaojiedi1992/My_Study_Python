class Point(object):
    def __init__(self,x,y) -> None:
        self.x = x 
        self.y = y 


def serialize_instance(point_obj):
    d = {'__classname__': type(point_obj).__name__}
    d.update(vars(point_obj))
    return d 

classMap = {
    'Point' : Point
}
def unserialize_object(d):
    clsname  = d.pop('__classname__',None)
    if clsname is None: 
        return  d 
    cls = classMap[clsname]
    obj = cls.__new__(cls)
    for k,v in d.items():
        setattr(obj,k,v)
    return obj 
p = Point(2,3)
import json 
s = json.dumps(p, default=serialize_instance)
print(s)
p = json.loads(s,object_hook=unserialize_object)
print(p.x)
