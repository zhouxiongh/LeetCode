#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        """ Gray(i) = i ^ (i/2) """
        num = 1 << n
        ans = [0] * num
        for i in range(num):
            ans[i] = (i >> 1) ^ i
        return ans
# @lc code=end

