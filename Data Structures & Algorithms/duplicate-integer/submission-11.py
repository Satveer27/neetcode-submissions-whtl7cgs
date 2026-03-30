class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicateHash = {}
        for i in nums:
            if i in hasDuplicateHash:
                return True
            else:
                hasDuplicateHash[i] = i
        return False