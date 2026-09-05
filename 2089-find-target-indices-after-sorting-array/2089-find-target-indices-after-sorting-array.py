class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums=sorted(nums)
        i=0
        index=[]

        while (i<len(nums)):
            if (nums[i]==target):
                index.append(i)
                i+=1
            else:
                i+=1
        return index