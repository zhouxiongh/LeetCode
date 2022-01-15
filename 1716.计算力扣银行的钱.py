#
# @lc app=leetcode.cn id=1716 lang=python3
#
# [1716] 计算力扣银行的钱
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        ans = sum(range(weeks+1, weeks + days + 1)) + (sum(range(8)) + sum(range(weeks, weeks+7))) * (weeks) // 2
        return ans

# @lc code=end

