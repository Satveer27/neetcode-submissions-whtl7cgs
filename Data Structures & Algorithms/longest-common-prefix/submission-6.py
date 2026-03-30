class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = strs[0]
        lng = ""
        isSub = True 
        for i in range(len(string)):
            for j in strs:
                if i == len(j):
                    isSub = False
                    break
                    
                if j[i] != string[i]:
                    isSub = False
                    break
            
            if isSub:
                lng += string[i]
            else:
                break
        
        return lng