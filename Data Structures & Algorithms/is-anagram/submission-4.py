class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashT = {}
        hashS = {}

        for i in s:
            if i in hashS:
                hashS[i] += 1
            else:
                hashS[i] = 0

        for i in t:
            if i in hashS:
                if i in hashT:
                    hashT[i] += 1
                else:
                    hashT[i] = 0
            else:
                return False
        
        for i in s:
            if hashT[i] != hashS[i]:
                return False
        
        return True
