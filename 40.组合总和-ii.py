#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
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
# @lc code=end

