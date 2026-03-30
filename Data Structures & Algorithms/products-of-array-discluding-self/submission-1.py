class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_sums = 1
        total_sums_without_0 = 1
        new_array = []
        total_0 = 0
        for i in nums:
            total_sums *= i
            if i!=0:
                total_sums_without_0 *= i
            
            if i==0:
                total_0 += 1
        
        for i in nums:
            if i==0:
                if total_0 >=2:
                    new_array.append(int(total_sums))
                else:
                    new_array.append(int(total_sums_without_0))

            else:
                new_array.append(int(total_sums/i))

        
        return new_array