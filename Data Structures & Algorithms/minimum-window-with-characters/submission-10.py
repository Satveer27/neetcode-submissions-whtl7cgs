class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        hashMapT = {}

        for i in t:
            if i in hashMapT:
                hashMapT[i] += 1
            else:
                hashMapT[i] = 1
            
        start = 0
        end = 0
        hashMapS = {}
        result = ""
        curr_length = None
        best_start = None
        best_end = None

        while start < len(s) and end < len(s):
            if s[start] not in hashMapT:
                if start == end:
                    end += 1

                if s[start] in hashMapS:
                    self.freq_check(hashMapS, s[start])

                start += 1

                if start < len(s) and s[start] in hashMapT and start > end:
                    end += 1
                    if start in hashMapS:
                        hashMapS[s[start]] += 1
                    else:
                        hashMapS[s[start]] = 1
            
                
            else:
                if len(hashMapS) == 0:
                    hashMapS[s[start]] = 1
                
                isValid = True

                for key in hashMapT:
                    if key in hashMapS:
                        if hashMapS[key] < hashMapT[key]:
                            isValid = False
                            break
                    else:
                        isValid = False
                        break
                
                if isValid:
                    if best_end is not None and best_start is not None:
                        length = end - start
                    if curr_length is None:
                        best_start = start
                        best_end = end + 1
                        curr_length = best_end - best_start
                    elif length < curr_length:
                        best_start = start
                        best_end = end + 1
                        curr_length = best_end - best_start
                    
             
                    self.freq_check(hashMapS, s[start])
                    start += 1

                    if start < len(s) and s[start] in hashMapT and start > end:
                        end += 1
                        if start in hashMapS:
                            hashMapS[s[start]] += 1
                        else:
                            hashMapS[s[start]] = 1

                
                else:
                    end += 1
                    if end < len(s):
                        if s[end] in hashMapS:
                            hashMapS[s[end]] += 1
                        else:
                            hashMapS[s[end]] = 1

            
        if best_end is not None:
            result = s[best_start:best_end]

        return result      



    def freq_check(self, hashMapS:dict, value:str):
        if value in hashMapS:
            hashMapS[value] -= 1

            if hashMapS[value] <= 0:
                hashMapS.pop(value)
