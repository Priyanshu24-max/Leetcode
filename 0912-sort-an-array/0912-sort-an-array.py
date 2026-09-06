class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        maximum=max(nums) # save the maximum value of the array
        minimum=min(nums) # save the minimum value of the array

        count=[0]*(maximum-minimum+1) # create a array of this much 0 in it

        for x in nums:
            count[x-minimum]+=1 # increase the value of that index if value is present

        i=0

        for x in range(len(count)):
            while(count[x]>0): # only enter loop if value is present at that index in count
                nums[i]=x+minimum #arrange value from smaller to larger
                i+=1
                count[x]-=1 # decreasing that value in count by 1 so we do not check that value again
        return nums