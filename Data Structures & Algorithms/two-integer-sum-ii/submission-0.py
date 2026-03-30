class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            check_num = target - numbers[i]
            for j in range(len(numbers)-1, i, -1):
                if numbers[j] == check_num:
                    return [i+1,j+1]
                
                if numbers[j] < check_num:
                    break

        return [0,0]