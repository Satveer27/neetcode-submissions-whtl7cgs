class Solution:
    #trying for optimised solution
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        bucketArray = [None] * len(nums)
        final_Array = []
        count = k
        
        for i in nums:
            if i in hashMap:
                hashMap[i] = hashMap[i] + 1
            else:
                hashMap[i] = 0
        
        
        for i in hashMap.items():
            if bucketArray[i[1]] is None:
                bucketArray[i[1]] = [i[0]]
            else:
                bucketArray[i[1]].append(i[0])
        
        
        for i in range(len(nums)):
            if count == 0:
                break
    
            if bucketArray[len(nums)-i-1] is not None:
                for i in bucketArray[len(nums)-i-1]:
                    if count == 0:
                        break

                    final_Array.append(i)
                    count -=1
        

        return final_Array