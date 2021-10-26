#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_size = len(matrix[0])
        size = len(matrix) * col_size
        l = 0
        r = size
        while l < r:
            mid = l + (r-l)//2
            if target == matrix[mid//col_size][mid%col_size]:
                return True
            if target < matrix[mid//col_size][mid%col_size]:
                r = mid
            else:
                l = mid + 1

        return False
# @lc code=end

