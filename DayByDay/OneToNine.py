# 九九乘法表 2021-01-26
# 题目 输出 9*9 乘法口诀表的一半
# 输出如下，要求每一行对齐
# 1*1=1  2*1=2  3*1=3  4*1=4  5*1=5  6*1=6  7*1=7  8*1=8  9*1=9
#        2*2=4  3*2=6  4*2=8  5*2=10 6*2=12 7*2=14 8*2=16 9*2=18
#               3*3=9  4*3=12 5*3=15 6*3=18 7*3=21 8*3=24 9*3=27
#                      4*4=16 5*4=20 6*4=24 7*4=28 8*4=32 9*4=36
#                             5*5=25 6*5=30 7*5=35 8*5=40 9*5=45
#                                    6*6=36 7*6=42 8*6=48 9*6=54
#                                           7*7=49 8*7=56 9*7=63
#                                                  8*8=64 9*8=72
#                                                         9*9=81



class Solution:
    def OneToNine(self):
        strres = ''
        for j in range(1, 10):
            for i in range(1, 10):
                if i == 9:
                    strres += str(i) + '*' + str(j) + '=' + str(i * j) + '\n'
                else:
                    if (len(str(i * j)) == 1):
                        strres += str(i) + '*' + str(j) + '=' + str(i * j) + '  '
                    else:
                        strres += str(i) + '*' + str(j) + '=' + str(i * j) + ' '
        print(strres)

    def OneToNinePlus(self):
        strres = ''
        for j in range(1, 10):
            for i in range(1, 10):
                if i >= j:
                    if i == 9:
                        strres += str(i) + '*' + str(j) + '=' + str(i * j) + '\n'
                    else:
                        if len(str(i * j)) == 1:
                            strres += str(i) + '*' + str(j) + '=' + str(i * j) + '  '
                        else:
                            strres += str(i) + '*' + str(j) + '=' + str(i * j) + ' '
                else:
                    strres += '       '
        print(strres)


su = Solution()
su.OneToNine()
su.OneToNinePlus()
