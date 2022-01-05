#
# @lc app=leetcode.cn id=1576 lang=python3
#
# [1576] 替换所有的问号
#

# @lc code=start
class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        list_str = list(s)

        for i in range(n):
            if list_str[i] == '?':
                for c in 'abc':
                    if not (i > 0 and list_str[i-1] == c or i < n -1 and list_str[i+1] == c):
                        list_str[i] = c
                        break
        return ''.join(list_str)
        
# @lc code=end

