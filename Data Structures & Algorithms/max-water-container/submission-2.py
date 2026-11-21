class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highest_area = None
        start_pointer = 0
        end_pointer = len(heights) - 1
        while start_pointer < end_pointer:
            if highest_area is None:
                area = (end_pointer - start_pointer) * min(heights[start_pointer], heights[end_pointer])
                highest_area = area
            else:
                area = (end_pointer - start_pointer) * min(heights[start_pointer], heights[end_pointer])
                if area > highest_area:
                    highest_area = area
                
            if heights[start_pointer] <= heights[end_pointer]:
                start_pointer += 1
            else:
                end_pointer -= 1
            
        
        return highest_area
                
