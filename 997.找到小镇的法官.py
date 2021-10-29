#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#
from typing import List
# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degrees = [0] * (n+1)
        for t in trust:
            degrees[t[0]] -= 1
            degrees[t[1]] += 1
        for i in range(1, n+1):
            if degrees[i] == n - 1:
                return i
        return -1

# @lc code=end

n = 3
trust = [[1,3],[2,3],[3,1]]
print(Solution().findJudge(n, trust))