# 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
#
# 作者：力扣 (LeetCode)
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nlen = len(nums)
        for i in range(0, nlen):
            if (nums[nlen - 1 - i] == 0) and (nlen - i <= nlen):
                for j in range(nlen - 1 - i, nlen):
                    if j + 1 < nlen:
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(nums)

    def moveZeroes2(self, nums: List[int]) -> None:
        if not nums:
            return 0
        j = 0
        for i in range(0, len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        print(nums)


su = Solution()
su.moveZeroes([1, 0, 3, 3, 1])
su.moveZeroes2([1, 0, 3, 3, 1])
