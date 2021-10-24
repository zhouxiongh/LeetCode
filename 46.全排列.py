#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(depth, cur=[]):
            if depth == n:
                ans.append(cur[:])
                return
            for i in range(n):
                if self.used[i]:
                    continue
                self.used[i] = True
                cur.append(nums[i])
                dfs(depth+1, cur)
                cur.pop()
                self.used[i] = False
        ans = []
        self.used = dict.fromkeys(range(len(nums)), False)
        n = len(nums)
        dfs(0)
        return ans
# @lc code=end
input_data = [1,2,3]
s = Solution()
output = s.permute(input_data)
print(output)

