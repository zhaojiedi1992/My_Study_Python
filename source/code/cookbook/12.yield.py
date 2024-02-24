from collections import deque
def count_down(n):
    while n > 0:
        print('T-minus', n)
        yield
        n -= 1
def count_up(n):
    x = 0
    while x < n:
        print('Counting up', x)
        yield
        x += 1

class TaskScheduler:
    def __init__(self) -> None:
        self.tasks =deque()

    def new_task(self,task):
        self.tasks.append(task)

    def run(self):
        while self.tasks:
            task = self.tasks.popleft()
            try:
                next(task)
                self.tasks.append(task)
            except StopIteration:
                pass

sched = TaskScheduler()
sched.new_task(count_down(10))
sched.new_task(count_down(5))
sched.new_task(count_up(15))
sched.run()