class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        start = 0
        end = len(heights) - 1
        while start < end:
            temp_area = 0
            width = (end+1) - (start+1)
            if heights[end] < heights[start]:
                temp_area = heights[end] * width
                if temp_area > area:
                    area = temp_area
                end -= 1
            else:
                temp_area = heights[start] * width
                if temp_area > area:
                    area = temp_area
                start += 1

        return area
