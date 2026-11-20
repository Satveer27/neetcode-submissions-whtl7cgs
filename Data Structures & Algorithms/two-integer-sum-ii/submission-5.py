class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first_pointer = 0
        second_pointer = len(numbers) - 1
        while first_pointer < second_pointer:
            lower_dif = target - numbers[second_pointer]

            if lower_dif == numbers[first_pointer]:
                return [first_pointer+1, second_pointer + 1]

            elif lower_dif > numbers[first_pointer]:
                first_pointer += 1
            
            else:
                second_pointer -= 1

    
