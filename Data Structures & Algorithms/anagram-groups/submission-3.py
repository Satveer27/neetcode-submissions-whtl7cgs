class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_array = []
        hashMap = {}
        count = 0
        for word in strs:
            curr_arr = [0] * 26

            for i in word:
                curr_arr[ord(i)% 26] = curr_arr[ord(i) % 26] + 1

            if tuple(curr_arr) in hashMap:
                final_array[hashMap[tuple(curr_arr)]].append(word)
            else:
                hashMap[tuple(curr_arr)] = count
                final_array.append([word])
                count += 1
        
        return final_array
              
    

                        


            
