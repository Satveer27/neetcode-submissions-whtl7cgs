class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        max_right = [0] * len(height)

        max_left_num = 0
        max_right_num = 0
        total = 0


        for num in height:
            if num > max_left_num:
                max_left_num = num
            
            max_left.append(max_left_num)

        
        for idx in range(len(height)-1, -1, -1):
            if height[idx] > max_right_num:
                max_right_num = height[idx]
            
            max_right[idx] = max_right_num
        
        
        for h_idx in range(len(height)):
            water_trap =  min(max_left[h_idx], max_right[h_idx]) - height[h_idx]
            print(water_trap)
            if water_trap >0:
                total += water_trap
        

        return total