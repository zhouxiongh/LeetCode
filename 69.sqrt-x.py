#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        guess_n = x
        # epsilon = 0.01
        while guess_n * guess_n > x :
            guess_n = (guess_n + x // guess_n) // 2
        return guess_n


# @lc code=end

