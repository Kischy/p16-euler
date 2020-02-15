# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:50:22 2019

@author: kisch
"""


import unittest

from sum_of_digits import calc_sum_of_digits as sod


class TestSumOfDigits(unittest.TestCase):
    
    def test_sum_of_digits(self):
        self.assertEqual(sod(32768),26)
        self.assertEqual(sod(1234),1+2+3+4)
        self.assertEqual(sod(56413),5+6+4+1+3)



if __name__ == '__main__':
    unittest.main(verbosity=0)
