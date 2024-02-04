def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


def countdown(n):
    print('start ')
    while n>0:
        yield n 
        n-=1
    print('done')
    

if __name__ == "__main__":
    for n in frange(0, 4, 0.5):
        print(n)
# symbol: frange
# hover info: (function) def frange(
#     start: Any,
#     stop: Any