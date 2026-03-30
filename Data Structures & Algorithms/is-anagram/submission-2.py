class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        for i in s:
            if i in hashS:
                hashS[i] = hashS[i] +  1
            else:
                hashS[i] = 1
        
        for j in t:
            if j in hashS:
                if j in hashT:
                    hashT[j] += 1
                else:
                    hashT[j] = 1
                
            else:
                return False
        

        for k in s:
            if k in hashS and k in hashT:
                if hashS[k] == hashT[k]:
                    continue
                else:
                    return False
            else: 
                return False
            
        return True