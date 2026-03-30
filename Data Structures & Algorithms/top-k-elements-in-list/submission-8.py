class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_hashmap = {}
        bucketArray = [None] * len(nums)
        final_Array = []

        for i in nums:
            if i in freq_hashmap:
                freq_hashmap[i] += 1
            else:
                freq_hashmap[i] = 0
        
        for key, value in freq_hashmap.items():
            if bucketArray[value] == None:
                bucketArray[value] = [key]
            else:
                bucketArray[value].append(key)
        
        if len(bucketArray)==1:
            for i in bucketArray[0]:
                final_Array.append(i)
            return final_Array

        for i in range(len(bucketArray)-1,-1,-1):
            if bucketArray[i] != None:
                for j in bucketArray[i]:
                    if k != 0:
                        final_Array.append(j)
                        k -= 1
                    else:
                        return final_Array

        return final_Array