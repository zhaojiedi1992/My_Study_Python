import time
from contextlib import contextmanager

@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))

# Example use
with timethis('counting'):
    n = 5
    while n > 0:
        n -= 1
        time.sleep(1)

import time

class timethisv2:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_ty, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start))



# Example use
with timethisv2('counting'):
    n = 5
    while n > 0:
        n -= 1
        time.sleep(1)

