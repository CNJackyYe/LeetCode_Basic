# 加一
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 解释：如整数99会表示为[9,9]这种形式，现在要写一个程序让99加1,即输出[1,0,0]
#
#
# 示例1：
#
# 输入：digits = [9,9]
# 输出：[1,0,0]
# 解释：输入数组表示数字 99。
# 示例2：
#
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 示例 3：
#
# 输入：digits = [0]
# 输出：[1]
#
#
# 提示：
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        inmark = 0
        dlen = len(digits)
        for i in range(0, dlen):
            inmark = 0
            digits[dlen - 1 - i] += 1
            if digits[dlen - 1 - i] == 10:
                digits[dlen - 1 - i] = 0
                inmark = 1
            else:
                break
        if inmark == 1:
            digits = [1] + digits
        print(digits)
        return digits


su = Solution()
su.plusOne([9, 9])
