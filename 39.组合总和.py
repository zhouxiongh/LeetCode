#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
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
# @lc code=end

