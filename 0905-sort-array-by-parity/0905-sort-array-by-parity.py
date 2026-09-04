class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        size=len(nums) #find the length of array

        for x in range(len(nums)):
            if(nums[x]%2==0):
                nums[x]=-nums[x] #convert all the even number into negative

        nums=sorted(nums) #sort them in acending order

        for i in range(size):
            if(nums[i]<0):
                nums[i]=-nums[i] # again convert them in postive 
        return nums