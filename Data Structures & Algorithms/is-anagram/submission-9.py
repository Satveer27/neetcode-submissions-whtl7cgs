class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmapS = {}
        hashmapT = {}

        for i in s:
            if i in hashmapS:
                hashmapS[i] += 1
            else:
                hashmapS[i] = 1
        
        for i in t:
            if i in hashmapT:
                hashmapT[i] += 1
            else:
                hashmapT[i] = 1
        
        for i in hashmapS:
            if i in hashmapT:
                if hashmapT[i] != hashmapS[i]:
                    return False
            else:
                return False
        return True
