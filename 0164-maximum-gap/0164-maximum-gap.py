class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums=sorted(nums)
        if(len(nums)<2):
            return 0
        else:
            best=0
            i,j=0,1
            
            while(i<j and j<len(nums)):
                best=max(best,abs(nums[j]-nums[i]))
                i+=1
                j+=1
            return best         