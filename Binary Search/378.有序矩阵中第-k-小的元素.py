#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第 K 小的元素
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l < r:
            m = (r+l) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l
# @lc code=end

