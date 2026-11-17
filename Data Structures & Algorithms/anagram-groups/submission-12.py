class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        final_result = []

        for word in strs:
            result = sorted(word)
            result = ''.join(result)
            if result not in hashMap:
                hashMap[result] = len(final_result)
                final_result.append([word])
            
            else:
                final_result[hashMap[result]].append(word)
        
        return final_result