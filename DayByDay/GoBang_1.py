# 五子棋_1 2021-1-29
# 制作一个可以下五子棋的面版（黑棋先手，白棋后手），并可以输入数字下棋，输入错误的数列会有提示
# 尽量不要去百度自己先想，我出的题都是一周一个系列的，利用前几天的知识去做题
# 如下
# ●请输入：12                         ○请输入：34                          ●请输入：35
#   1 2 3 4 5 6 7 8 9 a b c d e f     1 2 3 4 5 6 7 8 9 a b c d e f       1 2 3 4 5 6 7 8 9 a b c d e f
# 1 + ● + + + + + + + + + + + + +   1 + ● + + + + + + + + + + + + +     1 + ● + + + + + + + + + + + + +
# 2 + + + + + + + + + + + + + + +   2 + + + + + + + + + + + + + + +     2 + + + + + + + + + + + + + + +
# 3 + + + + + + + + + + + + + + +   3 + + + ○ + + + + + + + + + + +     3 + + + ○ ● + + + + + + + + + +
# 4 + + + + + + + + + + + + + + +   4 + + + + + + + + + + + + + + +     4 + + + + + + + + + + + + + + +
# 5 + + + + + + + + + + + + + + +   5 + + + + + + + + + + + + + + +     5 + + + + + + + + + + + + + + +
# 6 + + + + + + + + + + + + + + +   6 + + + + + + + + + + + + + + +     6 + + + + + + + + + + + + + + +
# 7 + + + + + + + + + + + + + + +   7 + + + + + + + + + + + + + + +     7 + + + + + + + + + + + + + + +
# 8 + + + + + + + + + + + + + + +   8 + + + + + + + + + + + + + + +     8 + + + + + + + + + + + + + + +
# 9 + + + + + + + + + + + + + + +   9 + + + + + + + + + + + + + + +     9 + + + + + + + + + + + + + + +
# a + + + + + + + + + + + + + + +   a + + + + + + + + + + + + + + +     a + + + + + + + + + + + + + + +      。。。。
# b + + + + + + + + + + + + + + +   b + + + + + + + + + + + + + + +     b + + + + + + + + + + + + + + +
# c + + + + + + + + + + + + + + +   c + + + + + + + + + + + + + + +     c + + + + + + + + + + + + + + +
# d + + + + + + + + + + + + + + +   d + + + + + + + + + + + + + + +     d + + + + + + + + + + + + + + +
# e + + + + + + + + + + + + + + +   e + + + + + + + + + + + + + + +     e + + + + + + + + + + + + + + +
# f + + + + + + + + + + + + + + +   f + + + + + + + + + + + + + + +     f + + + + + + + + + + + + + + +
#           步骤一                                步骤二                            步骤三                      以此类推


from typing import List

class Solution:
    def GoBang(self):
        Chess = []
        count = 0
        while 1:
            count += 1
            str = input(count % 2 == 1 and '●请输入：' or '○请输入：')
            if len(str) == 2:
                Chess = self.GeneralGoBang(str[0], str[1], count, Chess)
                #print(Chess)
            else:
                print('错误数据请重新输入')
                continue
            pass

    def GeneralGoBang(self, str1: str, str2: str, count: int, Chess: List[str]) -> List[str]:
        panChar = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        if panChar.__contains__(str1) & panChar.__contains__(str1):

            Chess.append([str1, str2, count % 2 == 1 and '●' or '○'])
            #colList = []
            #rowList = []
            printstr = ''
            for i in range(0, 16):
                for j in range(0, 16):
                    if i == 0:
                        # rowList.append(panChar[j])
                        printstr += panChar[j] + ' '
                    elif j == 0:
                        # rowList.append(panChar[i])
                        printstr += panChar[i] + ' '
                    else:
                        # rowList.append(self.CheckChess(str(i), str(j), Chess))
                        printstr += self.CheckChess(panChar[i], panChar[j], Chess) + ' '
                #colList.append(rowList)
                #rowList = []
                printstr+='\n'
                # print(colList[i])
            print(printstr)
        else:
            print('错误数据请重新输入')
        return Chess

    def CheckChess(self, i: str, j: str, Chess: List[str]):
        if Chess.__contains__([i, j, '●']):
            return '●'
        elif Chess.__contains__([i, j, '○']):
            return '○'
        else:
            return '+'
        pass


su = Solution()
su.GoBang()
