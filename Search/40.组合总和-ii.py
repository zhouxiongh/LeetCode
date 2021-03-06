#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, start, curr, ans):
            # find
            if target == 0:
                ans.append(curr[:])
                return

            for i in range(start, len(candidates)):
                # back up
                if candidates[i] > target: return
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                curr.append(candidates[i])
                dfs(candidates, target - candidates[i], i+1, curr, ans)
                curr.pop()

        ans = []
        candidates.sort()
        dfs(candidates, target, 0, [], ans)

        return ans



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, start, cur_ans, all_ans):
            if target == 0:
                all_ans.append(cur_ans[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    return
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                cur_ans.append(candidates[i])
                dfs(candidates, target - candidates[i], i+1, cur_ans, all_ans)
                cur_ans.pop()

        all_ans = []
        cur_ans = []
        candidates.sort()
        dfs(candidates, target, 0, cur_ans, all_ans)
        return all_ans

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, start=0, cur_ans=[]):
            if target == 0:
                ans.append(cur_ans[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    return
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                cur_ans.append(candidates[i])
                dfs(candidates, target-candidates[i], i+1, cur_ans)
                cur_ans.remove(candidates[i])
        ans = []
        candidates.sort()
        dfs(candidates, target)
        return ans



# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, target, ans, cur=[]):
            if target == 0:
                ans.append(cur[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    return
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                cur.append(candidates[i])
                dfs(i+1, target-candidates[i], ans, cur)
                cur.remove(candidates[i])
            return
        ans = []
        candidates.sort()
        dfs(0, target, ans)
        return ans
# @lc code=end