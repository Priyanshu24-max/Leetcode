class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=-1 #if number not present in array then it will return -1,-1
        last=-1

        low=0 #first index
        high=len(nums)-1 #last index

        while low<=high:
            mid=(low+high)//2 #find the middle value
            
            if(nums[mid]==target): #if mid value is equal to the target then we got the first index of target value
                first=mid #assign value of mid to first
                high=mid-1 #keep searching on the left side

            elif(target>nums[mid]):
                low=mid+1 #if target value is greater than value at mid then move towards rigth side
            else:
                high=mid-1 #else move towards left side

        low=0 
        high=len(nums)-1

        while low<=high: #again searching for last index
            mid=(low+high)//2
            
            if(nums[mid]==target):
                last=mid
                low=mid+1 #keep searching right side
            elif(target>nums[mid]):
                low=mid+1
            else:
                high=mid-1
            
        return [first,last] #return first and the last index