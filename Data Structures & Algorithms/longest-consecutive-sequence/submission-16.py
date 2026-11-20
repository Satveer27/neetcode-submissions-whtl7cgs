class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}  
        blackListMap = {}
        final_result = 0

        for i in nums:
            if i not in hashMap:
                hashMap[i] = 0

        for i in nums:
            consec = 1

            if i not in blackListMap:
                hasConsec = True
                blackListMap[i] = 0
                curr_value = i
                while hasConsec:
                    curr_value += 1
                    if curr_value in hashMap:
                        blackListMap[curr_value] = 0
                        consec += 1
                    else:
                        hasConsec = False
                        if consec > final_result:
                            final_result = consec
        
        
        return final_result
    
