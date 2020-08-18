# -*-coding:utf-8 -*-

'''
@File       : HJ26-字符串排序.py
@Author     : HW Shen
@Date       : 2020/8/17
@Desc       :

题目描述
编写一个程序，将输入字符串中的字符按如下规则排序。
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
如，输入： Type 输出： epTy
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
如，输入： BabA 输出： aABb
规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y
注意有多组测试数据，即输入有多行，每一行单独处理（换行符隔开的表示不同行）
'''


# 方法1：
# while True:
#     try:
#         string = input("please input string: ")
#         n = len(string)
#         result = [""] * n
#         chars = []  # chars用于提取英文字母
#         for i in range(n):
#             if string[i].isalpha():
#                 chars.append(string[i])
#
#         chars.sort(key=lambda ch: ch.lower())  # 对chars的字母统一大小写排序
#
#         for j in range(n):
#             if string[j].isalpha():
#                 result[j] = chars[0]
#                 chars.pop(0)
#             else:
#                 result[j] = string[j]
#
#         result = "".join(result)
#         print(result)
#
#     except:
#         break


# 方法2：
while True:
    try:
        string = input("please input string: ")
        n = len(string)
        # result = [""] * n
        chars = []  # chars用于提取英文字母
        for j in range(26):
            for i in range(n):
                if string[i].isalpha() and (ord(string[i])-ord("a") == j or ord(string[i])-ord("A") == j):
                    chars.append(string[i])
        # chars.sort(key=lambda ch: ch.lower())  # 对chars的字母统一大小写排序
        k = 0
        result = ""
        for m in range(n):
            if string[m].isalpha():
                result += chars[k]
                k += 1
            else:
                result += string[m]
        # result = "".join(result)
        print(result)

    except:
        break
