import os
dir = '.'
files = [ x for x in os.listdir() if os.path.isfile(os.path.join(dir, x))]
dirs = [x for x in os.listdir() if os.path.isdir(os.path.join(dir, x))]
print(files)
print(dirs)
pyfiles = [x for x in os.listdir() if os.path.isfile(x) and x.endswith('.py')]
print(pyfiles)

import glob
pyfiles = glob.glob('./*.py')
print('-'*20)
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name,meta in file_metadata:
    print(name,meta.st_size)