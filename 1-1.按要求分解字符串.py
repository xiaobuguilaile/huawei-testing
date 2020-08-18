# -*-coding:utf-8 -*-

'''
@File       : 1-1.按要求分解字符串.py
@Author     : HW Shen
@Date       : 2020/8/16
@Desc       :按要求分解字符串

 输入两个数 M，N；M代表输入的 M串字符串，N代表输出的每串字符串的位数，不够补0。
 例如：输入2, 8， “abc” ，“123456789”，则输出为“abc00000”,“12345678”,“90000000”

'''


# 解题思路：运用递归的方式，求解每一个字符串可能的拆分情况


def split_strs(M, N):

    strs = []
    for _ in range(M):
        inp_str = input("please input your string: ")
        strs.append(inp_str)

    newStr_list = []
    for str in strs:
        new_str = return_str(len(str), N, str)
        newStr_list += new_str

    return newStr_list


def return_str(n, N, str):

    if n <= N:
        return [str + "0" * (N - n)]
    else:
        return [str[:N]] + return_str(n-N, N, str[N:])


if __name__ == '__main__':

    newStr_list = split_strs(3, 5)

    print(newStr_list)

