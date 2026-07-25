class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(str(len(s)) + "!" + s)
        return "".join(parts)


    def decode(self, s: str) -> List[str]:
        newArray = []
        curr_index = 0
        while curr_index < len(s):
            num = ""
            while s[curr_index] != "!":
                num += s[curr_index]
                curr_index += 1

            newArray.append(s[curr_index+1: int(num)+curr_index+1])
            curr_index += (int(num) + 1)

        return newArray
    
            