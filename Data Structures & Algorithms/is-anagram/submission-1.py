class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        stringMap1 = {}
        stringMap2 = {}
        for c in s:
            if c in stringMap1:
                stringMap1[c] = stringMap1[c] + 1
            else:
                stringMap1[c] = 0
        
        for char in t:
            if char in stringMap2:
                stringMap2[char] = stringMap2[char] + 1
            else:
                stringMap2[char] = 0
        
        for key in stringMap1:
            if key not in stringMap2:
                return False
            if key in stringMap2:
                if stringMap1[key] != stringMap2[key]:
                    return False
        return True