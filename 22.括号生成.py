#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(l, r, cur):
            if l == 0 and r == 0:
                ans.append(cur)
                return
            if l > r:
                return

            if l > 0:
                cur += "("
                dfs(l-1, r, cur)
                cur = cur[:-1]
            if r > 0:
                cur += ")"
                dfs(l, r-1, cur)
                cur = cur[:-1]

            
        dfs(n, n, "")
        return ans
# @lc code=end

