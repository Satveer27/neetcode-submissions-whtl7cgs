class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap_initial = {}
        
        for i in nums:
            if i not in hashmap_initial:
                hashmap_initial[i] = 0
        
        curr_length = 0
        for i in nums:
            length = 0
            curr_value = i 
            if i-1 not in hashmap_initial:
                while curr_value in hashmap_initial:
                    length += 1
                    curr_value += 1
                
                if curr_length < length:
                    curr_length = length
        
        return curr_length
        