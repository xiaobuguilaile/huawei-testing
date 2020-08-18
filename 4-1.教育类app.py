# -*-coding:utf-8 -*-

'''
@File       : 4-1.教育类app.py
@Author     : HW Shen
@Date       : 2020/8/18
@Desc       :
'''

while True:

    try:
        res = 0
        char = input()
        curr_num = ""
        front_opr = ""
        while char != "=":
            if char != "+" and char != "-":
                curr_num += char
            else:
                if front_opr == "":
                    res += int(curr_num)
                    curr_num = ""
                elif front_opr == "+":
                    res += int(curr_num)
                    curr_num = ""
                elif front_opr == "-":
                    res -= int(curr_num)
                    curr_num = ""
                front_opr = char
            char = input()
        if front_opr == "+":
            res += int(curr_num)
        elif front_opr == "-":
            res -= int(curr_num)
        print(res)
    except:
        break

