class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        blanks = []
        for r in range(9):
            for c in range(9):
                s = board[r][c]
                if s != '.':
                    row[r].add(s)
                    col[c].add(s)
                    boxes[(r//3, c//3)].add(s)
                else:
                    blanks.append((r, c))
        def dfs():
            if not blanks:
                return True
            r, c = blanks.pop()
            for ans in [str(c) for c in range(1, 10)]:
                if not (ans in row[r] or ans in col[c] or ans in boxes[(r//3, c//3)]):
                    board[r][c] = ans
                    row[r].add(ans)
                    col[c].add(ans)
                    boxes[(r//3, c//3)].add(ans)
                    if dfs():
                        return True
                    board[r][c] = '.'
                    row[r].remove(ans)
                    col[c].remove(ans)
                    boxes[(r//3, c//3)].remove(ans)
                # back
            blanks.append((r, c))
            return False

        dfs()