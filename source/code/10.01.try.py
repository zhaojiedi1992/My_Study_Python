#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
try: 
    a =10 
    b =0 
    c =a/b 
except ZeroDivisionError as e :
    logging.exception(e)
else:
    print("no error")
finally: 
    print( "finally")
    