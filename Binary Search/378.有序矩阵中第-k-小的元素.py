#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第 K 小的元素
#


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
            m = l + (r - l) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l


# @lc code=end
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(val: int):
            i = n - 1
            j = 0
            num = 0
            while i >= 0 and j <= n - 1:
                if matrix[i][j] <= val:
                    num += i
                    j += 1
                else:
                    i -= 1
            return num >= k

        l = matrix[0][0]
        r = matrix[-1][-1]
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l


# @lc code=start
class Solution:
    def kthSmallest(self, matrix, k):
        def check(val):
            counter = 0
            row = n - 1
            col = 0
            while col < n and row >= 0:
                if val >= matrix[row][col]:
                    counter += row + 1
                    col += 1
                else:
                    row -= 1
            return counter >= k

        n = len(matrix)
        lo = matrix[0][0]
        hi = matrix[-1][-1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


# @lc code=end
