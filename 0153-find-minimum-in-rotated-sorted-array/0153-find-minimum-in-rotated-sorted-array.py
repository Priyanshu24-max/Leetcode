class Solution:
    def findMin(self, nums: List[int]) -> int:
        count=nums[0]
        i=1
        while(i<len(nums)):
            if(nums[i]<count):
                count=nums[i]
                i+=1
            else:
                i+=1
        return (count)
        