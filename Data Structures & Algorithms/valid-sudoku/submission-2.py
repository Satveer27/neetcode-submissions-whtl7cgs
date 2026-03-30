class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            hashMap = {}
            for column in row:
                if column != ".":
                    if column in hashMap:
                        return False
                    else:
                        hashMap[column] = 0
        
        for j in range(9):
            hashMap2 = {}
            for row in board:
                if row[j] != ".":
                    if row[j] in hashMap2:
                        return False
                    else:
                        hashMap2[row[j]] = 0
        
        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                seen = {}
                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        val = board[r][c]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen[val] = 1
        
        return True