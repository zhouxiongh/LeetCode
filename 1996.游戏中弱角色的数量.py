#
# @lc app=leetcode.cn id=1996 lang=python3
#
# [1996] 游戏中弱角色的数量
#

# @lc code=start
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        max_def = 0
        for _, def_ in properties:
            if def_ < max_def:
                ans += 1
            else:
                max_def = def_
        return ans
# @lc code=end

