import time

class Timer(object):
    def __init__(self):
        self.elapsed = 0 

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start


with Timer() as t:
    time.sleep(1)

print(t.elapsed)