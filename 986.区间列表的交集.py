#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            a, b = firstList[i]
            c, d = secondList[j]
            l = max(a, c)
            r = min(b, d)
            if l <= r:
                ans.append([l, r])
            if b < d:
                i += 1
            else:
                j += 1
        return ans
# @lc code=end

