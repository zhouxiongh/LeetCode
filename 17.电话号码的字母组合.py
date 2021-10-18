#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = ["", "", "abc", "def", "ghi", "jkl",
            "nmo", "pqrs", "tuv", "wxyz"]
        ans = [""]
        for digit in digits:
            tmp = []
            for s in ans:
                for c in d[ord(digit)-ord('0')]:
                    tmp.append(s+c)
            ans = tmp
        return ans
        
        
        
# @lc code=end

