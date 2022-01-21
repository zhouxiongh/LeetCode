#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        s1 = s2 = float('inf')
        for num in nums:
            if num <= s1:
                s1 = num
            elif num <= s2:
                s2 = num
            else:
                return True
        return False
# @lc code=end

