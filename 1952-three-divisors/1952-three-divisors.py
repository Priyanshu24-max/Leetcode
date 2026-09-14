class Solution:
    def isThree(self, n: int) -> bool:
        divisor=[i for i in range(1,n+1) if n%i==0] #store the factors of n

        if len(divisor)==3:
            return True
        else:
            return False