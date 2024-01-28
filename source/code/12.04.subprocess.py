#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

r = subprocess.call(["nslookup","www.python.org"])
print(r)

p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'python.org\nexit\n')
print(output.decode('utf-8'))
print(p.returncode)