from collections import defaultdict
from contextlib import contextmanager
class Exchange(object):
    def __init__(self) -> None:
        self.subscribers = set()

    def attach(self,task):
        self.subscribers.add(task)

    def detach(self,task):
        self.subscribers.remove(task)

    def send(self,msg):
        for subscriber in self.subscribers:
            subscriber.send(msg)

    def attach_tasks(self,*tasks):
        for task in tasks:
            self.attach(task)
    def detach_tasks(self,*tasks):
        for task in tasks:
            self.detach(task)
    def subscribe(self,task):
        self.attach(task)
    
    @contextmanager
    def subscribe_tasks(self,*tasks):
        self.attach_tasks(*tasks)
        try:
            yield
        finally:
            self.detach_tasks(*tasks)

    def clear(self):
        self.subscribers.clear()
    def get_subs(self): 
        return self.subscribers

_exchanges = defaultdict(Exchange)
def get_exchange(name):
    return _exchanges[name]

class Task:
    def send(self, msg):
        print(msg)

d = get_exchange('d')
t1 = Task()
t2 = Task()
d.attach(t1)
d.attach(t2)
d.send('hello')
d.send('world')
d.detach(t1)
print(d.get_subs())
d.clear()
print(d.get_subs())


with d.subscribe_tasks(t1,t2):
    d.send('hello')
    d.send('world')

print(d.get_subs())



