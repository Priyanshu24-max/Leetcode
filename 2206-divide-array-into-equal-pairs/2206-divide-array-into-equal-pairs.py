class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n=len(nums)/2
        count={}

        for x in nums:
            count[x]=count.get(x,0)+1

        result=[]

        for key,value in count.items():
            if value%2!=0: #if the frequence of value is not even then it cannot form a pair
                return False
        return True
                        