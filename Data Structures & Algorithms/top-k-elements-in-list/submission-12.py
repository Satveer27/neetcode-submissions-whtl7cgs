class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in nums:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        
        sorted_map = {k:v for k,v in sorted(hashMap.items(), key=lambda items: items[1], reverse=True)}

        final_result = []
        count = 0
        for key in sorted_map:
            final_result.append(key)
            count += 1
            if count == k:
                return final_result