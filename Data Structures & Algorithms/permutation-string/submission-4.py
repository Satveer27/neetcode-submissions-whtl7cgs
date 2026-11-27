class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

            
        s1_map = {}

        for i in s1:
            if i in s1_map:
                s1_map[i] += 1
            else:
                s1_map[i] = 1
        
        start = 0
        end = len(s1) -1
        s2_map = {}

        for i in range(len(s1)):
            if s2[i] in s2_map:
                s2_map[s2[i]] += 1
            else:
                s2_map[s2[i]] = 1

        while end < len(s2):
            isEqual = True
            for key in s2_map:
                if key in s1_map:
                    if s1_map[key] != s2_map[key]:
                        isEqual = False
                else:
                    isEqual = False
            
            if isEqual:
                return True
            else:
                print(s2_map)
                s2_map[s2[start]] -= 1

                if s2_map[s2[start]] == 0:
                    s2_map.pop(s2[start])
    
                end += 1
                start += 1
                if end < len(s2):
                    if s2[end] in s2_map:
                        s2_map[s2[end]] += 1
                    else:
                        s2_map[s2[end]] = 1
            

        return False
            
