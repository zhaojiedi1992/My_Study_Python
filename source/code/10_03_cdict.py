#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any


class CDict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try: 
            v = self[key]
        except KeyError as e :
             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, k: str, v: Any) -> None:
        self[k]=v
    