s = '{"name": "ACME", "shares": 50, "price": 490.1}'

import json 
from collections import OrderedDict

result = json.loads(s,object_pairs_hook=OrderedDict)
print(result)


class MyJosnObj(object):
    def __init__(self,d) -> None:
        self.__dict__ = d 
    
result = json.loads(s,object_hook=MyJosnObj)
print(result.name)
