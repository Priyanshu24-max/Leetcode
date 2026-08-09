class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums=sorted(nums)

        first=len(nums)-2
        second=len(nums)-1

        return ((nums[first]-1)*(nums[second]-1))