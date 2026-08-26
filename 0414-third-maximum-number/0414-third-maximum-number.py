class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))        
        first=second=third=float('-inf')

        for x in nums:
            if x>first:
                third=second
                second=first
                first=x
            elif(first>x>second):
                third=second
                second=x
            elif(second>x>third):
                third=x
        if(third==float('-inf')):
            return (first)
        else:
            return (third)         