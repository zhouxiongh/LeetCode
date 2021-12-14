#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs():
            if not blanks:
                return
            i, j = blanks.pop()
            for ans in [str(c) for c in range(1, 10)]:
                if ans not in rows[i] and ans not in cols[j] and ans not in boxes[(i//3, j//3)]:
                    board[i][j] = ans
                    rows[i].add(ans)
                    cols[j].add(ans)
                    boxes[(i//3, j//3)].add(ans)
                    if dfs() != False:
                        return
                    # backwards
                    board[i][j] = '.'
                    rows[i].remove(ans)
                    cols[j].remove(ans)
                    boxes[(i//3, j//3)].remove(ans)

            blanks.append((i, j))
            return False
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        blanks = []
        row_size = len(board)
        col_size = len(board[0])
        for i in range(row_size):
            for j in range(col_size):
                s  = board[i][j]
                if s == '.':
                    blanks.append((i, j))
                else:
                    rows[i].add(s)
                    cols[j].add(s)
                    boxes[(i//3, j//3)].add(s)
        dfs()

# @lc code=end

