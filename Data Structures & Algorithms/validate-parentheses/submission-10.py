class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
    
        hash_map = {")":"(", "}":"{", "]":"["}
        stack = []

        for i in s:
            if i not in hash_map:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                bracket = stack.pop()
                if hash_map[i] != bracket:
                    return False

        if len(stack) != 0:
            return False

        return True