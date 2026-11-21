class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_result_array = []
        sorted_nums = sorted(nums)

        for initial_idx in range(len(nums)):
            if initial_idx > 0 and sorted_nums[initial_idx] == sorted_nums[initial_idx-1]:
                continue 

            first_pointer = initial_idx + 1
            second_pointer = len(nums)-1

            while second_pointer > first_pointer:
                if first_pointer > (initial_idx + 1) and sorted_nums[first_pointer] == sorted_nums[first_pointer-1]:
                    first_pointer += 1
                    continue

                total = sorted_nums[initial_idx] + sorted_nums[first_pointer] + sorted_nums[second_pointer]
                if total == 0:
                    if sorted_nums[initial_idx] < sorted_nums[first_pointer]:
                        result = [sorted_nums[initial_idx], sorted_nums[first_pointer], sorted_nums[second_pointer]]
                    elif sorted_nums[initial_idx] > sorted_nums[second_pointer]:
                        result = [sorted_nums[first_pointer], sorted_nums[second_pointer], sorted_nums[initial_idx]]
                    else:
                        result = [sorted_nums[first_pointer], sorted_nums[initial_idx], sorted_nums[second_pointer]]
                    
                    final_result_array.append(result) 
                        
                    first_pointer += 1
                    second_pointer -= 1

                elif total < 0:
                    first_pointer += 1
                else:
                    second_pointer -= 1
            

        return final_result_array