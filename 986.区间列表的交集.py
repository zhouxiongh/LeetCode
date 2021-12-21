#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#

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

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList, secondList):
        ans = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                ans.append([lo, hi])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return ans
# @lc code=end