s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 }
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring

def dict2xml(tag,d):
    '''
    将字典转换为XML
    '''
    xml = ['<{}>'.format(tag)]
    for k,v in d.items():
        xml.append('<{0}>{1}</{0}>'.format(k,v))
    xml.append('</{}>'.format(tag))
    return '\n'.join(xml)

def dict2xmlv2(tag,d):
    elem = Element(tag)
    for k,v in d.items():
        child = Element(k)
        child.text = v 
        elem.append(child)
    return elem 

print(dict2xml("root",s))
e = dict2xmlv2("root",s)
print(tostring(e))
