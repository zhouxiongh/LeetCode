#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

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
                if (
                    ans not in rows[i]
                    and ans not in cols[j]
                    and ans not in boxes[(i // 3, j // 3)]
                ):
                    board[i][j] = ans
                    rows[i].add(ans)
                    cols[j].add(ans)
                    boxes[(i // 3, j // 3)].add(ans)
                    if dfs() != False:
                        return
                    # backwards
                    board[i][j] = "."
                    rows[i].remove(ans)
                    cols[j].remove(ans)
                    boxes[(i // 3, j // 3)].remove(ans)

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
                s = board[i][j]
                if s == ".":
                    blanks.append((i, j))
                else:
                    rows[i].add(s)
                    cols[j].add(s)
                    boxes[(i // 3, j // 3)].add(s)
        dfs()



# @lc code=start

class Solution:
    def solveSudoku(self, board):
        def dfs():
            if not blanks:
                return True
            # while blanks:
            i, j = blanks.pop()
            for s in [str(i) for i in range(1, 10)]:
                if s not in rows[i] and s not in cols[j] and s not in boxes[(i//3, j//3)]:
                    board[i][j] = s
                    rows[i].add(s)
                    cols[j].add(s)
                    boxes[(i//3, j//3)].add(s)
                    if dfs() == True:
                        return True
                    board[i][j] = "."
                    rows[i].remove(s)
                    cols[j].remove(s)
                    boxes[(i//3, j//3)].remove(s)
            blanks.append((i, j))
            return False


        blanks = []
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                s = board[i][j]
                if s == ".":
                    blanks.append((i, j))
                else:
                    rows[i].add(s)
                    cols[j].add(s)
                    boxes[(i//3, j//3)].add(s)
        dfs()
# @lc code=end