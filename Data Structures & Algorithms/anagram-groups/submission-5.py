class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for i in strs:
            arr = [0] * 26
            for j in range(len(i)):
                num = ord(i[j]) - ord("a")
                arr[num] += 1
            if tuple(arr) in hashMap:
                hashMap[tuple(arr)].append(i)
            else:
                hashMap[tuple(arr)] = [i]

        result = []

        for i,j in hashMap.items():
            result.append(j)
        return result

