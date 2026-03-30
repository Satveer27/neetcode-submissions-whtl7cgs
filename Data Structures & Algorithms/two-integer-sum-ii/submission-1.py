class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # optimized
        first_pointer = 0
        last_pointer = len(numbers) - 1
        for _ in range(len(numbers)-1):
            check_num = target - numbers[first_pointer]
            if check_num == numbers[last_pointer]:
                return[first_pointer+1, last_pointer+1]
            
            if check_num > numbers[last_pointer]:
                first_pointer += 1
            else:
                last_pointer -= 1
        
        return[0,0]