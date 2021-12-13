#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

class Solution:
    def combinationSum(self, candidates, target):
        def dfs(candidates, target, start, curr, ans):
            # find
            if target == 0:
                ans.append(curr[:])
                return

            for i in range(start, len(candidates)):
                # back up
                if candidates[i] > target: return
                curr.append(candidates[i])
                dfs(candidates, target - candidates[i], i, curr, ans)
                curr.pop()

        ans = []
        candidates.sort()
        dfs(candidates, target, 0, [], ans)

        return ans

# version 2
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start: int, cur_ans : List[int], all_ans: List[List[int]], target: int, candidates: List[int]):
            if target == 0:
                all_ans.append(cur_ans[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    return
                cur_ans.append(candidates[i])
                dfs(i, cur_ans, all_ans, target - candidates[i], candidates)
                cur_ans.pop()

        candidates.sort()
        all_ans = []
        cur_ans = []
        dfs(0, cur_ans, all_ans, target, candidates)
        return all_ans

# @lc code=start
# version 3
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = list()
        n = len(candidates)
        max_size = target // min(candidates) + 1
        for i in range(1, max_size):
            for c in itertools.combinations_with_replacement(candidates, i):
                if sum(c) == target:
                    ans.append(c)
        return ans
# @lc code=end

