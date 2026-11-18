class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += str(len(word)) + "#" + word
        
        return string

    def decode(self, s: str) -> List[str]:
        i = 0
        final_result = []

        while i <= len(s)-1:
            count = ""

            while s[i] != "#":
                count += s[i]
                i += 1
            
            final_result.append(s[i+1:i+1+int(count)])
            i = i + 1 + int(count)
        
        return final_result
