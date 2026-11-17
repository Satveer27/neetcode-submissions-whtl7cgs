class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapA = {}
        hashMapB = {}
        
        if len(s) != len(t):
            return False


        for letter in s:
            if letter in hashMapA:
                hashMapA[letter] += 1
            else:
                hashMapA[letter] = 1
        
        for letter in t:
            if letter in hashMapB:
                hashMapB[letter] += 1
            else:
                hashMapB[letter] = 1
        
        for letter in hashMapA:
            if letter not in hashMapB:
                return False

            if hashMapB[letter] != hashMapA[letter]:
                return False
        
        return True
                