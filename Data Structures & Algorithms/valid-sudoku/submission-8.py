class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            hashMapRow ={}
            for col in i:
                if col != ".":
                    if col in hashMapRow:
                        return False
                    else:
                        hashMapRow[col] = col
        
        for i in range(len(board[0])):
            hashMapCol={}
            for row in board:
                if row[i] != ".":
                    if row[i] in hashMapCol:
                        return False
                    else:
                        hashMapCol[row[i]] = row[i]

        for rowBox in range(0,9,3):
            for colBox in range(0,9,3):
                hashMap = {}
                for point in board[rowBox:rowBox+3]:
                    for point2 in point[colBox:colBox+3]:
                        if point2 != ".":
                            if point2 in hashMap:
                                return False
                            else:
                                hashMap[point2] = point2
        
        return True
