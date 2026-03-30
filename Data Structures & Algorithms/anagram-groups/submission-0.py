class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_result = []
        hashResult = {}
        count = 0
        for string in strs:
            key = ''.join(sorted(string))
            if key in hashResult:
                final_result[hashResult[key]].append(string)
            else:
                hashResult[key] = count
                final_result.append([string]) 
                count += 1
        return final_result