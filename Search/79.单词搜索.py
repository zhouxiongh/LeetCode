#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
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
# @lc code=end

