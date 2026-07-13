class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_hash = {}
        for i in range(len(nums)):
            sol = target - nums[i]
            if sol in new_hash:
                return [new_hash[sol], i]
            else:
                if nums[i] not in new_hash:
                    new_hash[nums[i]] = i

        