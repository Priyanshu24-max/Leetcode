class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        position=1

        for x in s:
            if 'a'<=x<='z':
                reverse_deg=ord('z')-ord(x)+1 #eg:- ord(z)=122 and ord(a)=97 so 122-97+1=26
                total+=position*reverse_deg
                position+=1
        return total