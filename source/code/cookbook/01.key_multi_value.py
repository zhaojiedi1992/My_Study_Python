d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}
e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}

def m1():
    result = {}
    for k,v in d.items():
        if k not in result: 
            result[k] =[]
        result[k].extend(v)
    for k,v in e.items():
        if k not in result: 
            result[k] =[]
        result[k].extend(v)
    print(result)

def m2(): 
    from collections import defaultdict
    result =defaultdict(list)
    for k,v in d.items():
        result[k].extend(v)
    for k,v in e.items():
        result[k].extend(v)
    print(result)
def m3(): 
  
    result ={}
    for k,v in d.items():
        result.setdefault(k,[]).extend(v)
    for k,v in e.items():
         result.setdefault(k,[]).extend(v)
    print(result)

if __name__ == "__main__": 
    m1()
    m2()
    m3()