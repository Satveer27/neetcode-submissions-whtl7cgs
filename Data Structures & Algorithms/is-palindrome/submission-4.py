class Solution:
    def isPalindrome(self, s: str) -> bool:
        NoSpaceString = ""

        for i in s:
            if i.isalnum():
                NoSpaceString += i.lower()
    
        start = 0
        end = len(NoSpaceString) - 1

        while start < end:
            if NoSpaceString[start] != NoSpaceString[end]:
                return False
            
            start += 1
            end -= 1

        return True