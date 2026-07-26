class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot = 1
        tot_zero = 1
        new_Array = []
        total_zero = 0
        for i in nums:
            if i != 0:
                tot = tot * i
                tot_zero = tot_zero * i
            else:
                tot_zero = 0
                total_zero += 1
        
        for i in nums:
            if i != 0:
                new_Array.append(int(tot_zero/i))
            else:
                if total_zero > 1:
                    new_Array.append(0)
                else:
                    new_Array.append(tot)
        
        return new_Array