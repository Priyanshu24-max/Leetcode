class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3 #return the element who appear more than n times

        count={} #to keep the count of number of times a particular number appears
        result=set() #to store number "if we take list than it may contain duplicates"

        for num in nums: 
            count[num]=count.get(num,0)+1 # in count ch gets the number of times ch appears and increase its value by 1 if ch not present then return 0
        for i,num in enumerate(nums): #loop through nums while getting both the index and the value where i stores the index and ch stores value
            if count[num]>n: #if the number of time value repeated id more than n then add it to result set
                result.add(num)
        return list(result)  