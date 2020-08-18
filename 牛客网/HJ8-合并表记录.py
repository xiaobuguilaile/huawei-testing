# -*-coding:utf-8 -*-

'''
@File       : HJ8-合并表记录.py
@Author     : HW Shen
@Date       : 2020/8/17
@Desc       :

题目描述
数据表记录包含表索引和数值（int范围的整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
输入描述:
先输入键值对的个数，然后输入成对的index和value值，以空格隔开
输出描述: 输出合并后的键值对（多行）
'''


# while True:
#     try:
#         stack = []
#         for _ in range(int(input())):
#
#             key_value = input().split(" ")
#             key, value = int(key_value[0]), int(key_value[1])
#
#             if len(stack) == 0:
#                 stack.append([key, value])
#             elif len(stack) == 1:
#                 if key == stack[0][0]:
#                     stack[0][1] += value
#                 else:
#                     output = stack.pop()
#                     print(output[0], output[1])
#                     stack.append([key, value])
#         print(stack[0][0], stack[0][1])
#     except:
#         break


from collections import Counter, defaultdict

while True:

    try:
        dic = defaultdict(int)
        for _ in range(int(input())):
            key_value = input().split(" ")
            key, value = int(key_value[0]), int(key_value[1])

            dic[key] += value

        for item in sorted(dic.items()):
            print(item[0], item[1])
    except:
        break






