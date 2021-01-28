# 画菱形 2021/1/28
# 题目 输入一个整数num，输出对应的菱形
# 如输入num=3
#   *
#  ***
# *****
#  ***
#   *
# 如输入num=4
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *


class Solution:
    def DrawDiamond(self, num: int):
        self.DrawSon(1, (num * 2 - 1))

    def DrawSon(self, num: int, total: int):
        if (num <= (total + 1) / 2):
            a = int((total + 1) / 2 - num) * ' ' + (num * 2 - 1) * '*'
            print(a)
        else:
            a = int(num - (total + 1) / 2) * ' ' + ((total + 1 - num) * 2 - 1) * '*'
            print(a)
        if (num <= total):
            self.DrawSon(num + 1, total)


su = Solution()
su.DrawDiamond(100)
