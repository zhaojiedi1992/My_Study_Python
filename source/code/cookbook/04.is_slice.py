def countdown(n):
    print('start ')
    while n>0:
        yield n 
        n-=1
    print('done')


if __name__ == "__main__":
    c = countdown(10)
    # c[0:3]

    import itertools
    res = itertools.islice(c,0,3)
    for i in res:
        print(i)
