class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxs=max(nums)
        mins=min(nums)

        gcd=[i for i in range(1,maxs+1) if maxs%i==0 and mins%i==0]

        return max(gcd) 