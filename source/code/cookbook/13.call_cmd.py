import subprocess

try:
    out_bytes = subprocess.check_output(['netstat','-a'], timeout=5,shell=True, stderr=subprocess.STDOUT)
except subprocess.TimeoutExpired as e:
    print(e)

import subprocess

# Some text to send
text = b'''
hello world
this is a test
goodbye
'''

# Launch a command with pipes
p = subprocess.Popen(['wc'],
          stdout = subprocess.PIPE,
          stdin = subprocess.PIPE)

# Send the data and get the output
stdout, stderr = p.communicate(text)

# To interpret as text, decode
out = stdout.decode('utf-8')
err =stderr.decode('utf-8')
