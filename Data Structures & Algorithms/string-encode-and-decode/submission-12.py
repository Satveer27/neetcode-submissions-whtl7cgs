class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ""
        for i in strs:
            new_str = str(len(i)) + "#" + i
            newString += new_str
        return newString

    def decode(self, s: str) -> List[str]:
        curLength = ""
        curStr = ""
        newList = []
        count = 0

        while count < len(s):
            if curLength == "":
                while s[count] != "#":
                    curLength += s[count]
                    count += 1
            else:
                curStr += s[count+1:count+int(curLength)+1]
                newList.append(curStr)
                curStr = ""
                count += int(curLength) + 1
                curLength = ""

        return newList
        
