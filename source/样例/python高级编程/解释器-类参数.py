class My_Decorator():
    def __init__(self,funciton,number=3):
        self.function=funciton
        self.number=number
    def __call__(self, *args, **kwargs):
        for i in range(self.number):
            result=self.function(*args,**kwargs)
            #return result

@My_Decorator
def foo():
    print("abc")


foo()