#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = [ch for ch in s]
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalpha():
                l += 1
                continue
            if not s[r].isalpha():
                r -= 1
                continue
            ans[l], ans[r] = ans[r], ans[l]
            l += 1
            r -= 1
        return "".join(ans)

# @lc code=end

