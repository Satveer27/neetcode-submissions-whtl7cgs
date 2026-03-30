class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(filter(str.isalnum, s))
        endPointer = len(s) - 1
        start = 0
        while start < endPointer:
            if s[endPointer] != s[start]:
                return False
            endPointer -= 1
            start += 1
            
        return True