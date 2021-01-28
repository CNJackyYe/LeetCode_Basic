# 五子棋_1 2021-1-29
# 制作如下的五子棋面版，并可以输入数字下棋

class Solution:
    def GoBang(self):
        panChar = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        colList = []
        rowList = []
        for i in range(0, 16):
            for j in range(0, 16):
                if i == 0:
                    rowList.append(panChar[j])
                elif j == 0:
                    rowList.append(panChar[i])
                else:
                    rowList.append('+')
            colList.append(rowList)
            rowList = []
            print(colList[i])
        pass

su = Solution()
su.GoBang()
