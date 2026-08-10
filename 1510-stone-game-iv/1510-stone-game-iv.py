class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        ans=[False]*(n+1)

        for i in range(1,(n+1)):
            j=1
            
            while(j*j<=i):
                if (ans[i-j*j]==False):
                    ans[i]=True
                    break
                j+=1
        return (ans[n])       