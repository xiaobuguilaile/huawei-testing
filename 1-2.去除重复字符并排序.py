# -*-coding:utf-8 -*-

'''
@File       : 1-2.去除重复字符并排序.py
@Author     : HW Shen
@Date       : 2020/8/16
@Desc       :

输入： 字符串
输出： 去除重复字符并排序的字符串
样例输入： aabcdefff
样例输出： abcdef
'''


# 解题思路： 先去重, 再排序

# 这里用了暴力排序，如果有时间复杂度的需要的话，可以使用快速排序


def remove_dupl_char(string:str):

    string = sorted(string)

    new_str = string[0]
    for i in range(1, len(string)):
        if string[i] != new_str[-1]:
            new_str += string[i]

    return new_str


if __name__ == '__main__':
    print(remove_dupl_char("wgraaaaaghhhhjoiiiiup"))

    # print(sorted("gwejorhalkf"))