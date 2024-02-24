from threading import Lock
class ShareCount(object):
    def __init__(self,start_cnt) -> None:
        self.start_cnt = start_cnt
        self.lock = Lock()

    def inc(self) -> None:
        with self.lock:
            self.start_cnt += 1

    def dec(self) -> None:
        self.lock.acquire()
        self.start_cnt -= 1
        self.lock.release()

    def get(self) -> int:
       
        return self.start_cnt
        

