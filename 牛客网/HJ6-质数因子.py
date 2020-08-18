# -*-coding:utf-8 -*-

'''
@File       : HJ6-质数因子.py
@Author     : HW Shen
@Date       : 2020/8/17
@Desc       :
'''

from math import sqrt


def factoring(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return i, num // i
    return num, None


def get_all_factors(num):
    n1, n2 = factoring(num)
    factors = [str(n1), ]

    while n2 is not None:
        n1, n2 = factoring(n2)
        factors.append(n1)
    print(" ".join(factors) + " ")


while True:
    try:
        num = int(input())
        get_all_factors(num)
    except:
        break