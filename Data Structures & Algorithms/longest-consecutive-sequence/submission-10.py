class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}

        if len(nums) == 0:
            return 0
            
        for i in nums:
            if i not in hashMap:
                hashMap[i]=i

        most_consecutive = 0   
        for i in nums:
            length = 1
            initial = i 

            if initial - 1 not in hashMap:
                while initial + 1 in hashMap:
                    length += 1
                    initial += 1
                
                if length > most_consecutive:
                    most_consecutive = length
        
        return most_consecutive 
        