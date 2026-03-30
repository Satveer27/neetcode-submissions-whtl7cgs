class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        max_l = []
        max_r = [0] * len(height)
        minlr = []

        cur_l = 0
        for i in range(len(height)):
            if i != 0:
                if height[i-1] > cur_l:
                    cur_l = height[i-1]
            max_l.append(cur_l)
        
        cur_r = 0
        for i in range(len(height)-1, -1, -1):
            if i != len(height)-1:
                if height[i+1] > cur_r:
                    cur_r = height[i+1]
        
            max_r[i] = cur_r
        
        for i in range(len(height)):
            minlr.append(min(max_l[i], max_r[i]))
        
        
        for i in range(len(height)):
            check = minlr[i] - height[i]
            if check > 0:
                count += check
          
        
        return count