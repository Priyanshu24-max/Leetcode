class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_Index=nums.index(max(nums))
        return max_Index       