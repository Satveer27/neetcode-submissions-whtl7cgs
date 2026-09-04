class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #row case
        for row in board:
            hashMapRow = {}
            for col in row:
                if col != ".":
                    if col in hashMapRow:
                        return False
                    else:
                        hashMapRow[col] = col
        
        # column case
        for col in range(9):
            hashMapCol = {}
            for row in board:
                if row[col] != ".":
                    if row[col] in hashMapCol:
                        return False
                    else:
                        hashMapCol[row[col]] = row[col]

        
        
        # Box case
        for row_box in range(0,9,3):
            for row_col in range(0,9,3):
                hashMapBox = {}
                for row in range(3):
                    for row_item in board[row_box + row][row_col:row_col+3]:
                        print(row_item)
                        print("")
                        if row_item != ".":
                            if row_item in hashMapBox:
                                return False
                            else:
                                hashMapBox[row_item] = row_item
                
        
        return True

                
                





    
                