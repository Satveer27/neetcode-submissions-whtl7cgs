class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        k = 0
        count = 0
        for i in nums:
            if count > 0:
                k = nums[count-1]
                if k == i:
                    return True
            count += 1
        return False
        