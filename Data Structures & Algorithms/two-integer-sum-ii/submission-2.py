class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            sol = numbers[start] + numbers[end]
            if sol == target:
                return [start + 1, end + 1]
            if sol > target:
                end -= 1
            else:
                start += 1

        return [0,0]