import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

def add(a,b):
    log.critical('add %s and %s', a, b)
    return a+b 

if __name__ == '__main__':
    logging.basicConfig()
    add(1,2)