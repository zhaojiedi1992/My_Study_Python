import gzip 
import glob 
import io 
from concurrent import futures
def find_robots(filename):
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f,encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots
def find_all_rebots(logdir):
    files = glob.glob(logdir+'/*.log.gz')
    rebots = set()
    # for robot in map(find_robots, files):
    #     rebots.update(robot)

    with futures.ProcessPoolExecutor() as pool:
        for robot in pool.map(find_robots, files):
            rebots.update(robot)

    return rebots

def hello(name):
    return f'Hello {name}'

def print_result(future):
    print(future.result())

if __name__ == '__main__':
    robots = find_all_rebots('logs')
    for ipaddr in robots:
        print(ipaddr)

    with futures.ProcessPoolExecutor() as pool:
        future_result= pool.submit(hello, 'world')
        future_result.add_done_callback(print_result)
