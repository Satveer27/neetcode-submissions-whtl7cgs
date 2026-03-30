class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        maxi = 0

        for i in nums:
            if maxi == 0:
                res = i
                maxi += 1
            else:
                if res == i:
                    maxi += 1
                else:
                    maxi -= 1
        
        return res