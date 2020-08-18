# -*-coding:utf-8 -*-

'''
@File       : test3.py
@Author     : HW Shen
@Date       : 2020/8/18
@Desc       :
'''


def judge(split_cakes):

    for i in range(len(split_cakes)-1):
        if split_cakes[i+1] - split_cakes[i] > 3:
            return False

        return True


from itertools import combinations

while True:
    try:
        count = 0
        nums = input().split(" ")
        m, n = int(nums[0]), int(nums[1])
        combs = list(combinations(range(n), m))
        for res in combs:
            if sum(res) == n and judge(res) and (0 not in res):
                # print(res)
                count += 1
        print(count)
    except:
        break


# count = 0
# m, n = 3, 12
# left_nums = n - m
# split_cakes = [1] * m
#
# tot = left_nums
# for i in range(1, m):
#     for j in range(i):
#         share_nums = tot-i+1-j  # 8
#         split_cakes[j] += share_nums  # 8
#         tot -= share_nums  # 9-8=1
