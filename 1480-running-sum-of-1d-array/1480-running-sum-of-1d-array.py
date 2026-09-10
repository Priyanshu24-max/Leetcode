class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for x in range(1,len(nums)):
            nums[x]+=nums[x-1]   # saving in current one the sum of previous and the current element
        return nums    