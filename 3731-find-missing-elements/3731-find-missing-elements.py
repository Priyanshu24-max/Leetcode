class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        size=nums[len(nums)-1]+1
        arr1=list(range(nums[0],size))
        nums=sorted(list(set(arr1)^set(nums)))
        return nums