class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums=sorted(nums)

        a=nums[0]*nums[1]*nums[-1] #taking two small and one large value as product of two neg is postive and if we multiply it by largest value the product will be max 
        b=nums[-1]*nums[-2]*nums[-3] #taking three largest value

        return max(a,b) # return maximum of a and b

        