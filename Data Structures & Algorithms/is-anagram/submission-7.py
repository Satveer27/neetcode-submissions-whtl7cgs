class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana1 = {}
        ana2 = {}

        for i in s:
            if i in ana1:
                ana1[i] += 1
            else:
                ana1[i] = 0
        
        for i in t:
            if i in ana2:
                ana2[i] += 1
            else:
                ana2[i] = 0    
        
        if len(ana1) != len(ana2):
            return False
        
        for i in ana1:
            if i in ana2:
                if ana1[i] != ana2[i]:
                    return False
            else:
                return False

        return True