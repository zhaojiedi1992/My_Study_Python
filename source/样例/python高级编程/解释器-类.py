class My_Decorator():
    def __init__(self,funciton):
        self.function=funciton
    def __call__(self, *args, **kwargs):
        print("start")
        result=self.function(*args,**kwargs)
        return result
        print("end")

@My_Decorator
def foo():
    print("abc")


foo()