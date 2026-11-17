class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for number in range(len(nums)):
            final = target - nums[number]
            if final in hashMap and hashMap[final] != number:
                return [hashMap[final], number]

            if nums[number] not in hashMap:
                hashMap[nums[number]] = number