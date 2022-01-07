#
# @lc app=leetcode.cn id=1614 lang=python3
#
# [1614] 括号的最大嵌套深度
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        l = 0
        for c in s:
            if c == '(':
                l += 1
                ans = max(ans, l)
            if c == ')':
                l -= 1
        return ans
# @lc code=end

