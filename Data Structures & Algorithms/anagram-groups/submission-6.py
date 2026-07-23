class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        count = 0
        finalArray = []
        for i in strs:
            if tuple(sorted(i)) in hashMap:
                finalArray[hashMap[tuple(sorted(i))]].append(i)
            else:
                hashMap[tuple(sorted(i))] = count
                finalArray.append([i])
                count += 1
        return finalArray