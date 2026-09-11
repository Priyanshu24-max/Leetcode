class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n=len(nums)/2
        count={}

        for x in nums:
            count[x]=count.get(x,0)+1

        result=[]

        for key,value in count.items():
            if value%2==0: #if the frequence of value if even then only it can form a pair
                result.append(True)
            else:
                result.append(False)
        if False in result: #if atleast one false is present that means there exist a value which cannot form a pair
            return False
        else:
            return True


        