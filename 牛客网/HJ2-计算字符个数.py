# -*-coding:utf-8 -*-

'''
@File       : HJ2-计算字符个数.py
@Author     : HW Shen
@Date       : 2020/8/17
@Desc       :
题目描述
写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。
输入描述:
第一行输入一个有字母和数字以及空格组成的字符串，第二行输入一个字符。
输出描述:
输出输入字符串中含有该字符的个数。
'''

# while True:
#
#     try:
#         string = input()
#         char = input()
#         dic = {}
#
#         for ch in string:
#             ch = ch.lower()
#             if ch in dic:
#                 dic[ch] += 1
#             else:
#                 dic[ch] = 0
#         if char in dic:
#             print(dic[char.lower()])
#         else:
#             print(0)
#
#     except:
#         break

# while True:
#
#     try:
#         string = input()
#         char = input()
#
#         from collections import Counter, defaultdict
#         dic = defaultdict()
#
#         for ch in string:
#             ch = ch.lower()
#             if ch in dic:
#                 dic[ch] += 1
#
#         if char in dic:
#             print(dic[char.lower()])
#         else:
#             print(0)
#
#     except:
#         break


if __name__ == '__main__':

    string = "nhrwlbcc8m7c5hih9mhalw98k0322wf2jjm47kk3ntm9snfrflzzundn7d608usy049asxalzjk7izj6amcqhr8uubc04g52mcjboj" \
             "2fmge2l6iarizfu4yve5o4i3srf5zgqbg82ckcotdeqp760mc9gzei5dzk5gj9x9yj05o3hle0ii64krkkp5i7blh7nbu3gu5vgi2sc" \
             "yn4yqx3z4vcjbyzhnqkh887izotjkg2l0mit0k14vyn39"
    char = "T"

    from collections import defaultdict

    dic = defaultdict(int)

    for ch in string:
        ch = ch.lower()
        dic[ch] += 1
    print(dic)

    print(dic[char.lower()])

