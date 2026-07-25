class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ""
        for i in strs:
            curr = str(len(i)) + "!" + i
            newString += curr
        return newString


    def decode(self, s: str) -> List[str]:
        newArray = []
        curr_index = 0
        while curr_index < len(s):
            num = ""
            for i in s[curr_index:]:
                if s[curr_index] != "!":
                    num += s[curr_index]
                    curr_index += 1
                else:
                    break

            newArray.append(s[curr_index+1: int(num)+curr_index+1])
            curr_index += (int(num) + 1)

        return newArray
            