def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

def add(x,y):
    return x+y 

def print_result(result):
    print("got result: {}".format(result))

apply_async(add,(2,3),callback=print_result)


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

r = ResultHandler()
apply_async(add,(2,3),callback=r.handler)
apply_async(add,(2,3),callback=r.handler)


def make_handler():
    sequence =0 
    while True:
        result = yield 
        sequence +=1 
        print('[{}] Got: {}'.format(sequence, result))

handler = make_handler()
next(handler)
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, (2, 3), callback=handler.send)

