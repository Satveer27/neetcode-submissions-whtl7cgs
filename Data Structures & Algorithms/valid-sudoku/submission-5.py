class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #1
        for i in board:
            hashMapRow = {}
            for j in i:
                if j != ".":
                    if j in hashMapRow:
                        return False
                    hashMapRow[j] = 0
        
        #2
        for i in range(9):
            hashMapCol = {}
            for j in board:
                if j[i] != ".":
                    if j[i] in hashMapCol:
                        return False
                    hashMapCol[j[i]] = 0
        
        #3
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                boxMap = {}
                
                for i in range(box_row, box_row+3):
                    for j in range(box_col, box_col+3):
                        if board[i][j] != ".":
                            if board[i][j] in boxMap:
                                return False
                            boxMap[board[i][j]] = 0
            

        return True