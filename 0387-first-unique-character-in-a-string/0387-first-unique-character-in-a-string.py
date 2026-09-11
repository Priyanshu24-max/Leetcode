class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}

        for x in s:
            count[x]=count.get(x,0)+1
        for key,value in count.items():
            if value==1: #if the value means number of the time the word repeats is 1 then return it 
                return s.index(key)
        return -1