#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, depth):
            if x < 0 or x == row_size or y < 0 or y == col_size:
                return False
            if board[x][y] != word[depth]:
                return False
            if depth == len(word) - 1:
                return True
            # four-way recur
            tmp = board[x][y]
            board[x][y] = 0
            ans = dfs(x-1, y, depth+1) or dfs(x+1, y, depth+1) or dfs(x, y-1, depth+1) or dfs(x, y+1, depth+1)
            board[x][y] = tmp
            return ans

        row_size = len(board)
        col_size = len(board[0])
        # find start char
        for i in range(row_size):
            for j in range(col_size):
                if dfs(i, j, 0):
                    return True
        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(row, col, depth, word):
            if row < 0 or row >= row_size or col < 0 or col >= col_size:
                return False
            if word[depth] != board[row][col]:
                return False
            if depth == len(word) - 1:
                return True
            tmp = board[row][col]
            board[row][col] = 0
            ans = dfs(row+1, col, depth+1, word) or dfs(row-1, col, depth+1, word) \
            or dfs(row, col+1, depth+1, word) or dfs(row, col-1, depth+1, word)
            board[row][col] = tmp
            return ans

        row_size = len(board)
        col_size = len(board[0])
        for i in range(row_size):
            for j in range(col_size):
                if dfs(i, j, 0, word):
                    return True
        return False

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, depth, word):
            if row < 0 or row >= row_size:
                return False
            if col < 0 or col >= col_size:
                return False
            if board[row][col] != word[depth]:
                return False
            if depth == len(word) - 1:
                return True
            tmp = board[row][col]
            board[row][col] = 0
            ans = dfs(row+1, col, depth+1, word) or dfs(row-1, col, depth+1, word) or dfs(row, col+1, depth+1, word) or dfs(row, col-1, depth+1, word)
            board[row][col] = tmp
            return ans
        row_size = len(board)
        col_size = len(board[0])
        for i in range(row_size):
            for j in range(col_size):
                if dfs(i, j, 0, word):
                    return True
        return False
# @lc code=end