class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        final_result = []
        for i in nums:
            if i in hashMap:
                hashMap[i] = hashMap[i] + 1
            else:
                hashMap[i] = 1

        srt = sorted(hashMap.items(), key=lambda x:x[1], reverse=True)
       
        for i in range(k):
            final_result.append(srt[i][0])
    
        return final_result