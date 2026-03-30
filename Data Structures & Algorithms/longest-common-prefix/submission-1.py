class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        initial_pref = ""
        for char in range(len(strs[0])):
            for word in strs:
                if len(word) == char or word[char] != strs[0][char]:
                    return initial_pref
                
            initial_pref = initial_pref + strs[0][char]
        return initial_pref

                