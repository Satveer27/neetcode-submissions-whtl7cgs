class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = []
        prefix = [1] * (len(nums))
        finalArray = []

        suf_prod = 1
        for i in nums:
            suffix.append(suf_prod*i)
            suf_prod *= i
        
        pref_prod = 1
        for i in range(len(nums)-1, -1, -1):
            pref_prod *= nums[i]
            prefix[i] = pref_prod

        for i in range(len(nums)):
            pref = 1
            suf = 1

            if i-1>=0:
                suf = suffix[i-1]
            if i + 1 < len(nums):
                pref = prefix[i+1]
            
            finalArray.append(pref*suf)


        return finalArray