class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        for i in s:
            if i in s_map:
                s_map[i] += 1
            else:
                s_map[i] = 1

        t_map = {}
        for i in t:
            if i in t_map:
                t_map[i] += 1
            else:
                t_map[i] = 1

        if len(t_map) != len(s_map):
            return False
            
        for i in t_map:
            if i in s_map:
                if t_map[i] != s_map[i]:
                    return False
            else:
                return False
        
        return True
