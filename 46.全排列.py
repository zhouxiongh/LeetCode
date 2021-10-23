#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(depth, curr, ans):
            if depth == n:
                ans.append(curr[:])
                return
            for i in range(n):
                if self.used[i]:
                    continue
                self.used[i] = True
                curr.append(nums[i])
                dfs(depth+1, curr, ans)
                curr.pop()
                self.used[i] = False
        ans = []
        self.used = dict.fromkeys(range(len(nums)), False)
        n = len(nums)
        dfs(0, [], ans)
        return ans
# @lc code=end
input_data = [1,2,3]
s = Solution()
output = s.permute(input_data)
print(output)

