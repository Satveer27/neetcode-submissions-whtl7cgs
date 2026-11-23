class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left_pointer = 0
        right_pointer = len(height)-1

        max_left = height[left_pointer]
        max_right = height[right_pointer]

        while left_pointer < right_pointer:
            result = 0
            if height[right_pointer] > max_right:
                    max_right = height[right_pointer]
                    
            if height[left_pointer] > max_left:
                    max_left = height[left_pointer]
            
            if height[left_pointer] < height[right_pointer]:
                result = min(max_left, max_right) - height[left_pointer]
                left_pointer += 1
            
            else:
                result = min(max_left, max_right) - height[right_pointer]
                right_pointer -= 1
            
            if result >0:
                total += result


        return total
                
    
                