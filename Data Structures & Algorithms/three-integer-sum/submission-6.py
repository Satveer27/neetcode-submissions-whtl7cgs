class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_result_map = {}
        sorted_nums = sorted(nums)

        for initial_idx in range(len(nums)):
            first_pointer = initial_idx + 1
            second_pointer = len(nums)-1

            while second_pointer > first_pointer:
                if second_pointer == initial_idx:
                    second_pointer -= 1
                elif first_pointer == initial_idx:
                    first_pointer += 1
                else:
                    total = sorted_nums[initial_idx] + sorted_nums[first_pointer] + sorted_nums[second_pointer]
                    if total == 0:
                        if sorted_nums[initial_idx] < sorted_nums[first_pointer]:
                            result = [sorted_nums[initial_idx], sorted_nums[first_pointer], sorted_nums[second_pointer]]
                        elif sorted_nums[initial_idx] > sorted_nums[second_pointer]:
                            result = [sorted_nums[first_pointer], sorted_nums[second_pointer], sorted_nums[initial_idx]]
                        else:
                            result = [sorted_nums[first_pointer], sorted_nums[initial_idx], sorted_nums[second_pointer]]
                        
                
                        if tuple(result) not in final_result_map:
                            final_result_map[tuple(result)] = 0
                        
                        first_pointer += 1
                        second_pointer -= 1

                    elif total < 0:
                        first_pointer += 1
                    else:
                        second_pointer -= 1
            
        final_result_array = []
        for key in final_result_map:
            final_result_array.append(key)

        return final_result_array