class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for x in range(len(nums)):
            if nums[x] in num_dict:
                return True

            else:
                num_dict[nums[x]] = nums[x]
                
        return False
        