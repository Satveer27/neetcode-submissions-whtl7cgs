class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ""
        for i in strs:
            newString += str(len(i)) + "#" + i
        return newString

    def decode(self, s: str) -> List[str]:
        new_array = []
        curr_len = ""
        count = 0
        print(s)
        while count < len(s):
            if s[count] !="#":
                curr_len = curr_len + s[count]
                count += 1
            else:
                if int(curr_len)==0:
                    new_array.append("")
                    count+=1
                else:
                    new_array.append(s[count+1:count+1+int(curr_len)])
                    count = count + 1 + int(curr_len)
                    curr_len = ""
                    if(count==len(s)):
                        break


        return new_array



