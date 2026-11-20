class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}  
        final_result = 0

        for i in nums:
            if i not in hashMap:
                hashMap[i] = 0

        for i in nums:
            consecs = 1
            if i - 1 not in hashMap:
                hasConsec = True
                curr_value = i
                while hasConsec:
                    curr_value += 1
                    if curr_value in hashMap:
                        consecs += 1
                    else:
                        if consecs > final_result:
                            final_result = consecs
                        hasConsec = False
                 
        return final_result
    
