class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = len(board)
        COL = len(board[0])
        seen = set()
        seen_row = set()
        seen_col = set()

        for i in range(ROW):
            for j in range(COL):


                curr = board[i][j]
                if curr.isdigit():
                    coordinates = (i//3,j//3,curr)
                    row_tup = (i,curr)
                    col_tup = (j,curr)

                    if coordinates in seen or row_tup in seen_row or col_tup in seen_col:
                        return False
                    
                    seen.add(coordinates)
                    seen_row.add(row_tup)
                    seen_col.add(col_tup)


                
        
        return True
        