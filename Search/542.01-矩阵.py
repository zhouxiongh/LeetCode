#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#


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
            for ni, nj in [
                (first - 1, second),
                (first + 1, second),
                (first, second - 1),
                (first, second + 1),
            ]:
                if ni < 0 or ni >= row_size or nj < 0 or nj >= col_size or seen[ni][nj]:
                    continue
                seen[ni][nj] = 1
                ans[ni][nj] = ans[first][second] + 1
                queue.append((ni, nj))
        return ans


# version 2
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row_size = len(mat)
        col_size = len(mat[0])
        queue = deque()
        # seen = set()
        ans = [[0] * col_size for i in range(row_size)]

        for i in range(row_size):
            for j in range(col_size):
                if mat[i][j] == 0:
                    # seen.add((i, j))
                    queue.append((i, j))
                else:
                    mat[i][j] = -1

        while queue:
            first, second = queue.popleft()
            for ni, nj in [
                (first - 1, second),
                (first + 1, second),
                (first, second - 1),
                (first, second + 1),
            ]:
                if (
                    ni < 0
                    or ni >= row_size
                    or nj < 0
                    or nj >= col_size
                    or mat[ni][nj] != -1
                ):
                    continue
                # seen.add((ni, nj))
                ans[ni][nj] = ans[first][second] + 1
                queue.append((ni, nj))
        return ans


# version3
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List:
        row_size = len(mat)
        col_size = len(mat[0])
        ans = [[0] * col_size for i in range(row_size)]
        queue = deque()

        for i in range(row_size):
            for j in range(col_size):
                if mat[i][j] == 0:
                    queue.append((i, j))

        while queue:
            i, j = queue.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if (
                    ni < 0
                    or ni >= row_size
                    or 0 > nj
                    or nj >= col_size
                    or mat[ni][nj] != 1
                ):
                    continue
                mat[ni][nj] = -1
                ans[ni][nj] = ans[i][j] + 1
                queue.append((ni, nj))

        return ans


class Solution:
    def updateMatrix(self, mat):
        n = len(mat)
        col_size = len(mat[0])
        new_mat = [[0] * col_size for i in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(col_size):
                if mat[i][j] == 0:
                    queue.append((i, j))
        while queue:
            row, col = queue.popleft()
            for i, j in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                if i in range(n) and j in range(col_size) and mat[i][j] != 0:
                    mat[i][j] = 0
                    new_mat[i][j] = new_mat[row][col] + 1
                    queue.append((i, j))
        return new_mat


# @lc code=start


class Solution:
    def updateMatrix(self, mat):
        row_size = len(mat)
        col_size = len(mat[0])
        new_mat = [[0] * col_size for i in range(row_size)]
        queue = deque()
        for i in range(row_size):
            for j in range(col_size):
                if mat[i][j] == 0:
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()
            for i, j in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                if 0 <= i < row_size and 0 <= j < col_size and mat[i][j] != 0:
                    mat[i][j] = 0
                    new_mat[i][j] = new_mat[row][col] + 1
                    queue.append((i, j))
        return new_mat


# @lc code=end
