class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        finalArray = []
        count = 0
        for i in strs:
            bigStr = [0] * 26
            for j in i:
                print((ord(j) - ord('a')))
                bigStr[(ord(j) - ord('a'))] += 1
            if tuple(bigStr) in hashMap:
                finalArray[hashMap[tuple(bigStr)]].append(i)
            else:
                hashMap[tuple(bigStr)] = count
                count += 1
                finalArray.append([i])
        
        return(finalArray)