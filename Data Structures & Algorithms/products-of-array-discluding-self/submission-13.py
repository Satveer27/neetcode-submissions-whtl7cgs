class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        postfix = [0] * len(nums)
        postfix_count = 1
        prefix_count = 1
        final_result = []

        for i in nums:
            prefix.append(prefix_count*i)
            prefix_count *= i

        for i in range(len(nums)-1, -1, -1):
            postfix[i] = postfix_count*nums[i]
            postfix_count *= nums[i]
        
        
        for i in range(len(nums)):
            post = 1
            pre = 1

            if i-1 >= 0:
                pre = prefix[i-1]
            
            if i+1 <= len(nums)-1:
                post = postfix[i+1]
            
            final_result.append(post*pre)
        
        return final_result
            
                