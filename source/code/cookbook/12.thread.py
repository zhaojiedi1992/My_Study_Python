
import time

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()


class CountDown(Thread):
    def __init__(self, n: int) -> None:
        super().__init__()
        self.n = n

    def run(self) -> None:
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

c = CountDown(5)
c.start()