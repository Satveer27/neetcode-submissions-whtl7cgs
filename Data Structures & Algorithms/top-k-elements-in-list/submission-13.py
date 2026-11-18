class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [None] * (len(nums)+1)
        hashMap = {}

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        for key,value in hashMap.items():
            idx = value % (len(nums)+1)
            if bucket[idx] is None:
                bucket[idx] = [key]
            else:
                bucket[idx].append(key)

        
        final_result = []
        count = 0
        for idx in range(len(bucket)-1, -1, -1):
            if bucket[idx] is not None:
                for result in bucket[idx]:
                    final_result.append(result)
                    count += 1
                    if count == k:
                        return final_result



