class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            point = target - nums[i]
            if point in hashMap:
                return [hashMap[point], i]
            
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
        
        return [0,0]