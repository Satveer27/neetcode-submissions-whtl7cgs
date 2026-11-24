class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        curr_stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):

            while len(curr_stack) != 0 and temperatures[curr_stack[-1]] < temperatures[i]:
                index = curr_stack.pop()
                result[index] = i-index
                
            curr_stack.append(i)
                
        return result