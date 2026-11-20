class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""

        for alpha in s:
            if alpha.isalnum():
                newString += alpha.lower()
        
        left_pointer = 0
        right_pointer = len(newString) - 1
        
        while left_pointer < right_pointer:
            if newString[left_pointer] != newString[right_pointer]:
                return False
            
            left_pointer += 1
            right_pointer -= 1
        
        return True