class Solution:
    def trap(self, height: List[int]) -> int:
        right_max_idx = 0

        left_max = 0
        total = 0

        for height_idx in range(len(height)):
            right_ptr = height_idx + 1
            if right_max_idx == height_idx and right_ptr<len(height):
                max_r = 0
                while right_ptr < len(height):
                    if max_r <= height[right_ptr]:
                        right_max_idx = right_ptr
                        max_r = height[right_ptr]
                    right_ptr += 1
            
                

            trapping_water = min(left_max, height[right_max_idx]) - height[height_idx]
            if trapping_water > 0:
                total += trapping_water
            
            if left_max < height[height_idx]:
                left_max = height[height_idx]
            
        return total
                
    
                