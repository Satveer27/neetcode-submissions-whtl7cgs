class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetHashmap = {}
        for i in range(len(nums)): 
            difference = target - nums[i]
            if (difference in targetHashmap):
                return [targetHashmap[difference], i]
            else:
                targetHashmap[nums[i]] = i

        return [0,0]

        


