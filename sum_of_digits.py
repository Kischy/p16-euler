# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:16:48 2019

@author: kisch
"""


def calc_sum_of_digits(number):
    sum_of_digits = 0
    
    while(number != 0):
        sum_of_digits += number % 10
        number //= 10
    
    return sum_of_digits

