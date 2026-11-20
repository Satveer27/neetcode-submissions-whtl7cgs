class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            hashMap = {}
            for values in row:
                if values != ".":
                    if values not in hashMap:
                        hashMap[values] = 0
                    else:
                        return False

        for column in range(len(board)):
            hashMap = {}
            for row in range(len(board)):
                if board[row][column] != ".":
                    if board[row][column] not in hashMap:
                        hashMap[board[row][column]] = 0
                    else:
                        return False
        
       
        for row_box in range(0,9,3):
            for col_box in range(0,9,3):
                hashMap = {}
                for row in board[row_box:row_box+3]:
                    for column in row[col_box:col_box+3]:
                        if column != ".":
                            if column not in hashMap:
                                hashMap[column] = 0
                            else:
                                return False
        
        return True
            





