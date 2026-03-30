class Solution:
    def isPalindrome(self, s: str) -> bool:
        endPointer = len(s) - 1
        start = 0
        while start < endPointer:
            while start < endPointer and not s[start].isalnum():
                start += 1
            
            while endPointer>start and not s[endPointer].isalnum():
                endPointer -= 1

            if s[endPointer].lower() != s[start].lower():
                return False
            endPointer -= 1
            start += 1
            
        return True