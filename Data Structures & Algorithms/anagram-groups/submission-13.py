class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        TOTAL_ALPHABETS = 26

        hashMap = {}
        result = []
        for word in strs:
            array = [0] * TOTAL_ALPHABETS
            for letter in word:
                array[(ord(letter)-ord("a"))] += 1
        
            if tuple(array) not in hashMap:
                hashMap[tuple(array)] = len(result)
                result.append([word])
            else:
                result[hashMap[tuple(array)]].append(word)

        return result