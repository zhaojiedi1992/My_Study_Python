# import re
# NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
# NUM = r'(?P<NUM>\d+)'
# PLUS = r'(?P<PLUS>\+)'
# TIMES = r'(?P<TIMES>\*)'
# EQ = r'(?P<EQ>=)'
# WS = r'(?P<WS>\s+)'

from ply.lex import lex 
from ply.yacc import yacc 

# master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

tokens = ['NAME', 'NUM', 'PLUS', 'TIMES', 'EQ', 'WS']

t_PLUS = r'\+'
t_TIMES = r'\*'
t_EQ = r'='
t_ignore = ' \t'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)


text = '1 + 2 * 3 = '
lexer = lex(debug=0)
lexer.input(text)

for tok in iter(lexer.token, None):
    print(tok)


