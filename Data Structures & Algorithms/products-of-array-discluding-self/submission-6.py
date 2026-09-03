class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        newArray = []
        zero_count = 0
        for i in nums:
            if i == 0:
                zero_count += 1

            if i != 0:
                prod *= i
            
        for i in nums:
            if i == 0 and zero_count > 1:
                newArray.append(0)
            elif i ==0 and zero_count <= 1:
                newArray.append(prod)
            elif i != 0  and zero_count > 0:
                newArray.append(0)
            else:
                newArray.append(int(prod/i))
        
        return newArray