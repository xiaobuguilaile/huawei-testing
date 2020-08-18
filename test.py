# -*-coding:utf-8 -*-

'''
@File       : test.py
@Author     : HW Shen
@Date       : 2020/8/17
@Desc       :
第一题： 对几个硬盘按照内存大小排序
输入： 第一行为 硬盘数量，后面每行为 每个硬盘的大小 (单位是M,G,T的组合形势)， eg. 3M2G, 1024M, 5G12M, 2T15M
输出： 按从小到大的顺序输出 (注意同等大小的硬盘（eg.1024M 和 1G），需要保序输出）
'''

while True:
    try:
        comp_li = []
        for _ in range(int(input())):
            string = input()
            a = ""
            total_v = 0
            for ch in string:
                if ch.isdigit():
                   a += ch
                else:
                    if ch == "T":
                        total_v += int(a)*1024*1024
                    elif ch == "G":
                        total_v += int(a)*1024
                    elif ch == "M":
                        total_v += int(a)
                    a = ""
            comp_li.append([string, total_v])
        print("comp_li: ", comp_li)
        items = sorted(comp_li, key=lambda x: x[1])
        print("items:", items)
        for item in items:
            print(item[0])
    except:
        break


if __name__ == '__main__':
    print("1".isdigit())

    # import sys
    # # 读取第一行的n
    # n = int(sys.stdin.readline().strip())
    # ans = 0
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = list(map(int, line.split()))
    #     for v in values:
    #         ans += v
    # print(ans)