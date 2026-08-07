import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Initialize data structures to track 'seen' numbers
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r // 3, c // 3)

        # 2. Iterate through every cell in the 9x9 grid
        for r in range(9):
            for c in range(9):
                # Skip empty cells
                if board[r][c] == ".":
                    continue
                
                # 3. Identify the current value and its sub-box coordinates
                val = board[r][c]
                square_id = (r // 3, c // 3)

                # 4. Check for duplicates in the current row, column, or square
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[square_id]):
                    return False
                
                # 5. Add the value to our 'seen' sets
                rows[r].add(val)
                cols[c].add(val)
                squares[square_id].add(val)

        return True