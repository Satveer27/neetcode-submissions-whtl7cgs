class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += str(len(word)) + "#" + word
        
        return string

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        print(s)
        count = None
        curr_count = 0
        curr_string = ""
        final_result = []
        isCount = False

        for i in s:
            if count is None:
                count = str(i)
                isCount = True
            
            elif isCount and i == "#":
                isCount = False
                count = int(count)

            elif isCount and i != "#":
                count += str(i)

            else:
                if int(count) == 0:
                    final_result.append("")
                    count = i
                    isCount = True

                elif curr_count == int(count):
                    final_result.append(curr_string)
                    count = i
                    curr_count = 0
                    curr_string = ""
                    isCount = True
            
                else:
                    curr_count += 1
                    curr_string += str(i)


        final_result.append(curr_string)
        return final_result
            