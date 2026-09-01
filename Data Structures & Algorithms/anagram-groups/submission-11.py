class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        finalArray = []
        count=0
        for i in strs:
            freqArray = [0] * 26
            for letters in i:
                freqArray[(ord(letters) - ord("a"))] += 1

            if tuple(freqArray) in hashMap:
                finalArray[hashMap[tuple(freqArray)]].append(i)
            else:
                hashMap[tuple(freqArray)]= count
                finalArray.append([i])
                count += 1

        return finalArray