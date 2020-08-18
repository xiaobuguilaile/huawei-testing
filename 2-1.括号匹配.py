# -*-coding:utf-8 -*-

'''
@File       : 2-1.括号匹配.py
@Author     : HW Shen
@Date       : 2020/8/16
@Desc       :

给定一个字符串，里边可能包含“()”、“[]”、“{}”三种括号，请编写程序检查该字符串中的括号是否成对出现，且嵌套关系正确。
输出：true:若括号成对出现且嵌套关系正确，或该字符串中无括号字符；
false:若未正确使用括号字符。
实现时，无需考虑非法输入。

例子：(1+2)/(0.5+1)
输出描述： True
'''

# 解题思路：栈
# 遇到左符号，则压入，遇到右符号，弹出顶层的符号和右符号比对，如果符合，则继续，否则输出false


def whatType(ch:str):
    """ 判断char类型 """
    if ch == "[" or ch == "{" or ch == "(":
        return -1
    elif ch == "]" or ch == "}" or ch == ")":
        return 1
    else:
        return 0


def ifFit(a:str, b:str):
    """ 判断前后符号是否为成对的括号 """
    if a == "{" and b == "}": return 1
    if a == "[" and b == "]": return 1
    if a == "(" and b == ")": return 1
    return 0


def bracket_match(query:str):

    characters = []  # 栈
    for char in query:
        if whatType(char) == -1:
            # 如果是左边符号，就压入栈顶
            characters.append(char)
        elif whatType(char) == 1:
            if len(characters) == 0:  # 栈为空
                return False  # 如果为右符号，且栈中无左符号，失败
            else:  # 栈不为空
                if ifFit(characters[len(characters)-1], char) == 0:
                    return False  # 如果为右符号，但是无法配对，失败
                else:
                    characters.pop()  # 如果为右符号，且左右配对成功，就弹出栈顶端的左符号

    if len(characters) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    query = "(1+2}[/](0.5+1{})()"
    print(bracket_match(query))
