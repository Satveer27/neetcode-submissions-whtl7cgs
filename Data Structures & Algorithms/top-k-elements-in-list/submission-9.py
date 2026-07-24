class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums))]
        hashMap = {}
        finalArray = []
        for i in nums:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 0
    
        for i in hashMap:
            bucket[(hashMap[i] % len(nums))].append(i)
            
        
        count = k
    
        for i in range(len(bucket)-1, 0-1, -1):
            if len(bucket[i]) !=0:
                for j in bucket[i]:
                    finalArray.append(j)
                    count -= 1
                    if count == 0:
                        return finalArray

        return finalArray
         