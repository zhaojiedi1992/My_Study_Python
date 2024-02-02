#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse 

def main(): 
    
    p = argparse.ArgumentParser(
        prog='backup',
        description='backup db',
        epilog='copyright ,2023'
    )
    p.add_argument('outfile')
    p.add_argument('--host',default='localhost')
    p.add_argument('--port',default=3306,type=int)
    p.add_argument('-u', '--user', required=True)
    p.add_argument('-p', '--password', required=True)
    p.add_argument('--database', required=True)
    p.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')

    args = p.parse_args()
    print(args)


if __name__ == '__main__':
    # (venv) ➜  My_Study_Python git:(master) ✗ python3 ./source/code/14.03.argparse.py  -uroot -poracle --database d1 -gz a.txt
    # Namespace(outfile='a.txt', host='localhost', port=3306, user='root', password='oracle', database='d1', gzcompress=True)
    main()