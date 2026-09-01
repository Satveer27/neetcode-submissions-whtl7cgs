class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        hashMap = {}
        for i in nums:
            residue = target - i
            if residue in hashMap:
                return [hashMap[residue], count]
            
            if i not in hashMap:
                hashMap[i] = count
        
            count += 1

        return [0,0]
            
                
