class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            hashRow = {}
            for col in row:
                if col != ".":
                    if col in hashRow:
                        return False

                    hashRow[col] = 0
        
        for col in range(9):
            hashCol = {}
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] in hashCol:
                        return False
                    hashCol[board[row][col]] = 0
        
        for row_box in range(0,9,3):
            for col_box in range(0,9,3):
                hashCheck = {}
                for row in board[row_box: row_box+3]:
                    for col in row[col_box: col_box+3]:
                        if col != ".":
                            if col in hashCheck:
                                return False
                            hashCheck[col] = 0
        return True



