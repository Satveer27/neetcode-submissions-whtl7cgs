class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        max_length = 1
        freq_arr = [0]*26

        while end < len(s) and start < len(s):
            freq_arr[ord(s[end]) - ord("A")] += 1

            current_highest = 0
            for i in freq_arr:
                current_highest = max(current_highest, i)
            
            window_len = end - start +1
            if window_len - current_highest <= k:
                end += 1

            else:
                freq_arr[ord(s[end]) - ord("A")] -= 1
                freq_arr[ord(s[start]) - ord("A")] -= 1
                start += 1
                window_len -= 1 
            
            max_length = max(max_length, window_len)

        return max_length


