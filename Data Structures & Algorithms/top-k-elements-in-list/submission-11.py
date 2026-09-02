class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        bucket = [None] * len(nums)
        for i in nums:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 0
        
        for key in hashMap:
            index = hashMap[key] % len(nums)
            if bucket[index] is not None:
                bucket[index].append(key)
            else:
                bucket[index] = [key]
        
        count = k 
        finalArray = []
        for i in range(len(nums)-1, -1, -1):
            if count != 0 :
                if bucket[i] is not None:
                    for j in bucket[i]:
                        finalArray.append(j)
                        count -= 1
        
        return finalArray
            