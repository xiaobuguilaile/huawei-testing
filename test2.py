# -*-coding:utf-8 -*-

'''
@File       : test2.py
@Author     : HW Shen
@Date       : 2020/8/18
@Desc       :
第二题： 匹配字符串
要求从字符串t中找出第一个字符串p 对应在t中的下标（注意：下标从1开始算起），规定 字符串 t比 p 长
输入： 第一行为字符串 t， 第二行为字符串 p
输出： 对应的下标
举例：
输入的两行为：
AVERDXIVYERDIAN
RDXI
输出为：
4
'''

while True:

    try:
        t = input()
        p = input()
        nt, np = len(t), len(p)

        for i in range(len(t)):
            if len(t) - i < len(p):
                print("No")
                break
            if p == t[i:i+np]:
                print(i+1)
                break
    except:
        break

# AVERDXIVYERDIAN
# RDXI