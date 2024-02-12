def sample():
    n =0 
    def func():
        print('n={}'.format(n))
    
    def get_n():
        return n 
    def set_n(value):
        nonlocal n 
        n =value 
    func.get_n = get_n
    func.set_n = set_n
    return func

f = sample()
f()
f.set_n(10)
f()
f.get_n()