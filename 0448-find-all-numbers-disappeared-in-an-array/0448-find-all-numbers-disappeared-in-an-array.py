class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)

        for x in nums:  #this loop is to store all the index of nums except those number which are not present with neg sign
            index=abs(x)-1
            nums[index]=-abs(nums[index]) 
        
        result=[]

        for i in range(n):
            if nums[i]>0:
                result.append(i+1) #append the number which are not present in list
        return result
