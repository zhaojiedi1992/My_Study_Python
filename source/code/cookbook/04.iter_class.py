from collections import deque
class linehistory(object):
    def __init__(self,lines,max_size) -> None:
        self.lines = lines 
        self.max_size = max_size
        self.history = deque(maxlen=self.max_size)
    
    def __iter__(self):
        for lineno,line in enumerate(self.lines,1):
            self.history.append((lineno,line))
            yield line 
        
    def clear(self):
        self.history.clear()

if __name__ == "__main__":
    with open('./somefile.txt') as f:
        lines = linehistory(f,3)
        for line in lines:
            if 'python' in line:
                for lineno,hline in lines.history:
                    print(f'{lineno}:{hline}')
