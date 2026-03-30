class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        endPointer = len(newStr) - 1
        start = 0
        while start < endPointer:
            if newStr[endPointer] != newStr[start]:
                return False
            endPointer -= 1
            start += 1
            
        return True