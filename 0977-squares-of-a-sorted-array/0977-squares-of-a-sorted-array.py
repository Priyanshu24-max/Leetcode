class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0

        while(i<=len(nums)-1):
            nums[i]=nums[i]**2
            i+=1
        nums.sort()
        return (nums)        