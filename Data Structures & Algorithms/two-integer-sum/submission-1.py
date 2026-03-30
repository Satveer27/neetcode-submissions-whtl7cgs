class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetHashmap = {}
        index = -1
        smallerindex = -1
        bigNumber = 0
        smallNumber = 0
        for i in nums: 
            difference = target - i
            if(difference in targetHashmap):
                bigNumber = difference
                smallNumber = i
                break
            else:
                targetHashmap[i] = i

        for num in range(len(nums)):
            if nums[num] == smallNumber and num != index and smallerindex == -1:
                smallerindex = num
                continue

            if nums[num] == bigNumber and num != smallerindex:
                print(num)
                index = num
                continue
        
        if index < smallerindex:
            return[index,smallerindex]
        
        return [smallerindex, index]
            


