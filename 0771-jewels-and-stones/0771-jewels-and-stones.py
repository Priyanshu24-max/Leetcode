class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        je=set(jewels)
        st=list(stones)
        count=0

        for x in st:
            if x in je:
                count+=1
        return count        