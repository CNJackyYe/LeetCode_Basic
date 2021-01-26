# 数字组合 2021-01-27
# 题目 有四个数字：0、1、2、3，能组成多少个互不相同且无重复数字的三位整数？各是多少？
# 请由小到大输出
# 输入如下
# [102, 103, 120, 123, 130, 132, 201, 203, 210, 213, 230, 231, 301, 302, 310, 312, 320, 321]

class Solution:
    def NumComb(self):
        nums = [0, 1, 2, 3]
        res = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                for k in range(0, len(nums)):
                    if (i != j) & (j != k) & (i != k):
                        num = i * 100 + j * 10 + k
                        if (num > 100) & (res.count(num) == 0):
                            res.append(num)
        print(res)

su = Solution()

su.NumComb()
