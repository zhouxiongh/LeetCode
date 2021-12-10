#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float('inf')
        n = len(nums)
        dp = [0] * (n+1)
        i = 1
        for n in nums:
            dp[i] = max(dp[i-1]+n, n)
            ans = max(dp[i], ans)
            i += 1
        return ans
# @lc code=end
nums = [-1]
assert -1 == Solution().maxSubArray(nums)
