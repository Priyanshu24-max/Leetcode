class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        ans=[0]*2*n
        while(i<=n-1):
            ans[i]=(nums[i])
            ans[n+i]=(nums[i])
            i+=1
            
        return (ans)