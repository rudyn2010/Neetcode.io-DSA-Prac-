class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Straightforward solution process, look at a snapshot perspective, according to problem board can be valid but not solvable
        # Use of sets to determine whether or not there is 1 unique value in each row, column, or square
        
        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                   board[r][c] in columns[c] or
                   board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True