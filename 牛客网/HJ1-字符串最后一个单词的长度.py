# -*-coding:utf-8 -*-

'''
@File       : HJ1-字符串最后一个单词的长度.py
@Author     : HW Shen
@Date       : 2020/8/17
@Desc       :

'''


# 方法1：
while True:
    try:
        string = input()
        count = 0
        for i in range(len(string)-1,-1,-1):
            if string[i].isalpha():
                count += 1
            else:
                if count >= 1:
                    break
                count = 0
        print(count)
    except:
        break

# 方法2：
while True:
    try:
        string = input()
        strs = string.split(" ")
        print(strs[-1])
    except:
        break