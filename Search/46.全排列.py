#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import List
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
input_data = [1,2,3]
s = Solution()
output = s.permute(input_data)
print(output)


# version 2

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(cur_depath, cur_ans, all_ans, depth):
            if cur_depath == depth:
                all_ans.append(cur_ans[:])
                return
            for i in range(depth):
                if i in self.used:
                    continue
                self.used.add(i)
                cur_ans.append(nums[i])
                dfs(cur_depath+1, cur_ans, all_ans, depth)
                cur_ans.pop()
                self.used.remove(i)
        self.used = set()
        all_ans = []
        cur_ans = []
        n = len(nums)

        dfs(0, cur_ans, all_ans, n)
        return all_ans


# @lc code=start
class Solution:
    def permute(self, nums: List[int]):
        return list(itertools.permutations(nums))

# @lc code=end