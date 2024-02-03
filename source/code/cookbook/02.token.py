import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pat.scanner('foo = 42')

for m in iter(scanner.match,None):
    print(m.lastgroup,m.group())
# NAME foo
# WS  
# EQ =
# WS  
# NUM 42