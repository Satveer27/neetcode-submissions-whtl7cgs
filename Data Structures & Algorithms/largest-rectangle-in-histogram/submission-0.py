class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        
        stack = []
        current_max_height = 0

        for idx in range(len(heights)):
            curr_idx = idx
            while len(stack) != 0 and heights[idx] < stack[-1][1]:
                index, height = stack.pop()
                width = idx - index
                current_max_height = max(height * width, current_max_height)
                curr_idx = index
                
            
            stack.append((curr_idx, heights[idx]))

        return current_max_height


        