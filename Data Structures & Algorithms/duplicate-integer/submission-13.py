class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newHashMap = {}
        
        for i in range(len(nums)):
            if nums[i] not in newHashMap:
                newHashMap[nums[i]] = i
            else:
                return True

        return False