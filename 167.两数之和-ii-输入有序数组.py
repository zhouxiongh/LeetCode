#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if target == s:
                return [l+1, r+1]

            if target < s: 
                r -= 1
            else:
                l += 1
        return [-1, -1]
# @lc code=end

