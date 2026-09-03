class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        subArray1 = []
        subArray2 = [0] * len(nums)
        finalArray = []

        point_forward = 1
        for i in nums: 
            subArray1.append(point_forward * i)
            point_forward = point_forward * i
        
        point_backward = 1
        for i in range(len(nums)-1, -1, -1):
            subArray2[i] = point_backward * nums[i]
            point_backward = point_backward * nums[i]
        
    
        for i in range(len(nums)):
            if i-1 < 0:
                finalArray.append(subArray2[i+1])
            
            elif i+1 >= len(nums):
                finalArray.append(subArray1[i-1])

            else:
                finalArray.append(subArray1[i-1] * subArray2[i+1])
        
        return finalArray

