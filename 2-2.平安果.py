# -*-coding:utf-8 -*-

'''
@File       : 2-2.平安果.py
@Author     : HW Shen
@Date       : 2020/8/17
@Desc       :

给定一个 M行 N列 的矩阵（M*N个格子），每个格子中放着一定数量的平安果。
你从左上角的格子开始，只能向下或者向右走，目的地是右下角的格子。
每走过一个格子，就把格子上的平安果都收集起来。求你最多能收集到多少平安果。
注意：当经过一个格子时，需要一次性把格子里的平安果都拿走。
限制条件：1<N, M<=50；每个格子里的平安果数量是0到1000（包含0和1000）.

输入描述：第一行 M和 N，接下来M行，每行都包含N个平安果数量
输出描述：一个整数，即最多拿走的平安果的数量
'''

# 解题思路： 动态规划
# 当前位置可以获得的最大平安果 = 横向能获得的最大平安果数 + 纵向能获得的最大平安果数


def max_apples(m, n, matrix):

    if m == 0 and n == 0:
        return matrix[0][0]
    elif m == 0:
        return matrix[m][n] + max_apples(m, n-1, matrix)
    elif n == 0:
        return matrix[m][n] + max_apples(m-1, n, matrix)
    else:
        return max(matrix[m][n] + max_apples(m-1, n, matrix), matrix[m][n] + max_apples(m, n-1, matrix))


if __name__ == '__main__':

    M, N = 4, 5
    m, n = M-1, N-1  # 行列转下标

    matrix = [[0, 5, 0, 1, 0 ],
              [6, 1, 0, 11, 0],
              [0, 2, 0, 0, 8 ],
              [10, 0, 0, 3, 0]]
    print(max_apples(m, n, matrix))

