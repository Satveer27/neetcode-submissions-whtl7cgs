class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        all_prod = 1
        has_zero = 0

        for i in nums:
            if i == 0:
                has_zero += 1
            else:
                all_prod *= i

            if has_zero >= 2:
                all_prod = 0
                break
            
        for i in nums:
            if i == 0:
                result.append(all_prod)

            elif has_zero >= 1:
                result.append(0)
            
            else:
                result.append(int(all_prod/i))
        
        return result