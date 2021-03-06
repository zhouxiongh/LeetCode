#
# @lc app=leetcode.cn id=1220 lang=python3
#
# [1220] 统计元音字母序列的数目
#

# @lc code=start
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        M = 10 ** 9 + 7
        for _ in range(n-1):
            a, e, i, o, u = (e + i + u) % M, (a + i) % M, (e + o) % M, i % M, (i + o) % M
        return sum([a, e, i, o, u]) % M

# @lc code=end

