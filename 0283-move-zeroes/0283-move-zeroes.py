class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        original=nums.copy()
        size1=len(nums)
        nums.clear()

        for x in original:
            if (x!=0):
                nums.append(x)
        size2=len(nums)

        for x in range(0,size1-size2):
            nums.append(0)
        
        