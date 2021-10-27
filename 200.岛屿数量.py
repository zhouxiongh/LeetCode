#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
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
# @lc code=end

