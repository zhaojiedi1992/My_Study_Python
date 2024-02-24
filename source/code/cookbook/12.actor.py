from queue import Queue
from threading import Event, Thread

class ActorExit(Exception):
    pass
class Actor(object):
    def __init__(self) -> None:
        self.queue = Queue()
        self._terminated = Event ()
        self.task = None

    def close(self):
        self.queue.put(ActorExit)

    def send(self, msg):
        self.queue.put(msg)

    def recv(self):
        msg = self.queue.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def start(self):
        # self.event.set()
        self.task = Thread(target=self._bootstrap)
        self.task.daemon = True
        self.task.start()
        pass

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()
                

    def run(self):
        raise NotImplementedError

    def join(self):
        self._terminated.wait()

class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print('Got:', msg)


p = PrintActor()
p.start()
p.send('Hello')
p.send('World')
p.close()
p.join()
