#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
from typing import List
# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(target, k, cur=0, cur_sum=0):
            if k == 0:
                return True
            if cur_sum == target:
                return dfs(target, k-1)
            for i in range(cur, len(nums)):
                if used[i]:
                    continue
                used[i] = True
                cur_sum += sorted_nums[i]
                if dfs(target, k, i, cur_sum):
                    return True
                cur_sum -= sorted_nums[i]
                used[i] = False
            return False
        s = sum(nums)
        used = [False] * len(nums)
        sorted_nums = sorted(nums)
        if s % k != 0:
            return False
        return dfs(s // k, k)
# @lc code=end
s = Solution()
# input1 = [4,3,2,3,5,2,1]
# input2 = [3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269]
input3 = [1,2,3,5]
input4 = [4,3,2,3,5,2,1]
# print(s.canPartitionKSubsets(input1, 4))
# print(s.canPartitionKSubsets(input2, 5))
# print(s.canPartitionKSubsets(input3, 2))
print(s.canPartitionKSubsets(input4, 4))

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(target, k, start=0, cur_sum=0):
            if k == 0:
                return True
            if cur_sum == target:
                return dfs(target, k-1)
            for i in range(start, len(nums)):
                if i in used: continue
                used.add(i)
                cur_sum += nums[i]
                if dfs(target, k, i, cur_sum):
                    return True
                used.remove(i)
                cur_sum -= nums[i]
            return False

        s = sum(nums)
        used = set()
        if s % k != 0:
            return False
        return dfs(s//k, k)
