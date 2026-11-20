class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        final_result = 0
        current_highest = 0
        prev_data = None
        print(sorted_nums)
        for i in sorted_nums:
            if prev_data is None:
                final_result += 1
            elif prev_data != i and (prev_data + 1) == i:
                final_result += 1
            elif prev_data + 1 != i and prev_data != i:
                final_result = 1
            
            if final_result > current_highest:
                current_highest = final_result

            prev_data = i
        
        return current_highest
        
