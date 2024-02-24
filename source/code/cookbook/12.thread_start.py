
import time
from threading import Thread, Event

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()


class CountDown(Thread):
    def __init__(self, n: int,event) -> None:
        super().__init__()
        self.n = n

    def run(self) -> None:
        print('Countdown is running 1')
        event.set()
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

event = Event()
c = CountDown(5,event)
c.start()

event.wait()
print('Countdown is running 2 ')