def countdown(n):
    print('start ')
    while n>0:
        yield n 
        n-=1
    print('done')


from itertools import dropwhile
res = dropwhile(lambda n:n>=5,countdown(10))
for i in res:
    print(i)
