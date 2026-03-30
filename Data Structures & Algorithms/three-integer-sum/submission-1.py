class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        for i in range(len(nums)-1):
            if i>0 and nums[i] == nums[i-1]:
                continue
                
            pointer1 = len(nums) - 1
            pointer2 = i + 1
    
            while pointer1 > pointer2:
                total = nums[i] + nums[pointer1] + nums[pointer2] 
                if total == 0:
                    out.append([nums[i], nums[pointer1] , nums[pointer2]])
                    pointer1-=1
                    while nums[pointer1] == nums[pointer1+1] and pointer1>pointer2:
                        pointer1-=1
                elif total > 0:
                    pointer1 -= 1
                else:
                    pointer2 += 1
            
        return out
          