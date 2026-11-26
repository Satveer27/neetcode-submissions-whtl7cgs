class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_length = 1
        hashMap = {}
        start_index = 0

        for idx in range(len(s)):
            if s[idx] in hashMap and hashMap[s[idx]] >= start_index:
                start_index = hashMap[s[idx]] + 1
                hashMap[s[idx]] = idx
            else:
                hashMap[s[idx]] = idx
               
            max_length = max(max_length, idx - start_index+1)

        return max_length

        