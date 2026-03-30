class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_array = []
        count = 0
        hashMap = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in hashMap:
                final_array[hashMap[key]].append(word)
            else:
                final_array.append([word])
                hashMap[key] = count
                count += 1
          


        return final_array
                


            
