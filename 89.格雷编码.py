#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        s = 2 << (n-1)
        ans = [i for i in range(s)]
        for i in range(s):
            ans[i] = i // 2 ^ i
        return ans

# @lc code=end

