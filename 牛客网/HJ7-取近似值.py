# -*-coding:utf-8 -*-

'''
@File       : HJ7-取近似值.py
@Author     : HW Shen
@Date       : 2020/8/17
@Desc       :

题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
输入描述: 输入一个正浮点数值
输出描述: 输出该数值的近似整数值
'''


while True:
    try:

        string = input()
        nums = string.split(".")
        if int(nums[1][0]) >= 5:
            print(int(nums[0]) + 1)
        else:
            print(int(nums[0]))

    except:
        break