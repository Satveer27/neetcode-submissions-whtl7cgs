class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        suf = 1
        pref = 1
        for i in range(1,len(nums)):
            pref *= nums[i-1]
            output[i] = pref
        
        for i in range(len(nums)-2, -1, -1):
            suf *= nums[i+1]
            output[i] = suf * output[i]

        return output
