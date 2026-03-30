class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashResult = {}
        size = int(len(nums)/2)
        for i in range(size+1):
            if nums[i] in hashResult:
                hashResult[nums[i]] = hashResult[nums[i]] + 1
            else:
                hashResult[nums[i]] = 1

        final_result = nums[0]
        for i in hashResult:
            if hashResult[final_result] < hashResult[i]:
                    final_result = i
        
        return final_result
