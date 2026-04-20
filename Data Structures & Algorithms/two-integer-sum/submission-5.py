class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                pass
            else:
                hashMap[nums[i]] = i
        
        for i in range(len(nums)-1, -1, -1):
            check = target - nums[i]
            if check in hashMap:
                return [hashMap[check], i]

        return []