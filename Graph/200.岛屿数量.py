#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        col_size = len(grid[0])
        row_size = len(grid)
        def dfs(x, y):
            if x < 0 or x >= row_size or y < 0 or y >= col_size or grid[x][y] != "1":
                return
            grid[x][y] = "0"
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
        ans = 0
        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)

        return ans
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if row < 0 or row >= row_size or col < 0 or col >= col_size:
                return
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
        ans = 0
        row_size = len(grid)
        col_size = len(grid[0])
        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        return ans

# @lc code=start
class Solution:
    def numIslands(self, grid):
        def dfs(row, col):
            if row < 0 or row >= row_size or col < 0 or col >= col_size or grid[row][col] != "1":
                return
            grid[row][col] = "0"
            for i, j in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                dfs(i, j)
        ans = 0
        row_size = len(grid)
        col_size = len(grid[0])
        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        return ans
# @lc code=end