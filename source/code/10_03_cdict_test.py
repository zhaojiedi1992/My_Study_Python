#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from 10_03_cdict import CDict

class TestDict(unittest.TestCase):
     def test_init(self):
        d = CDict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))


