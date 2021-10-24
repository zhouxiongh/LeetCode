#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row_size = len(mat)
        col_size = len(mat[0])
        ans = [[0] * col_size for j in range(row_size)]
        seen = [[0] * col_size for j in range(row_size)]
        queue = deque()
        # find 0
        for i in range(row_size):
            for j in range(col_size):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    seen[i][j] = 1
        # bfs
        while queue:
            first, second = queue.popleft()
            for ni, nj in [(first-1, second), (first+1, second), (first, second-1), (first, second+1)]:
                if ni < 0 or ni >= row_size or nj < 0 or nj >= col_size or seen[ni][nj]:
                    continue
                seen[ni][nj] = 1
                ans[ni][nj] = ans[first][second] + 1
                queue.append((ni, nj))
        return ans

# @lc code=end

