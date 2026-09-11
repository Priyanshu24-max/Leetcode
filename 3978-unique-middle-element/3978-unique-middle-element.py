class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid=len(nums)//2 # to find the index of middle element

        seen={nums[mid]} #add middle element to this 

        count=0 # to count how many time middle element repeat
        
        for x in nums:
            if x in seen: #if x value is equal to the middle element then increase it by one
                count +=1

        if count>1: #as it should be repeated only one time if the count is more than one then output becomes false
            return False
        else:
            return True  
        