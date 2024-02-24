from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_url(url):
    u = requests.get(url)
    return u.text

pool = ThreadPoolExecutor(10)
# Submit work to the pool
a = pool.submit(fetch_url, 'http://www.python.org')
b = pool.submit(fetch_url, 'http://www.pypy.org')

# Get the results back
x = a.result()
y = b.result()

print(x,y)
