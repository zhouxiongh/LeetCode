#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            ans = max(ans, h * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans

# @lc code=end

