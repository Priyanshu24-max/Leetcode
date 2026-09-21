class Solution:
    def arrangeCoins(self, n: int) -> int:
        low,high=1,n 
        while low<=high:
            mid=(high+low)//2
            num=(mid+1)*(mid/2) #calculating the total number of coins needed to build mid complete rows.

            if num<=n:
                low=mid+1
            else:
                high=mid-1
        return high