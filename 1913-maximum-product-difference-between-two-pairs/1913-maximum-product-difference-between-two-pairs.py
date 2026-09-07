class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums=sorted(nums)        
        size=len(nums)-1
        prod_diff=(nums[size]*nums[size-1])-(nums[0]*nums[1])

        return prod_diff