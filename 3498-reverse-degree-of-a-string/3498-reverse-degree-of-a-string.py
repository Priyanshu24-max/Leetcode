class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        postion=1

        for x in s:
            if 'a'<=x<='z':
                reverse_deg=ord('z')-ord(x)+1 #eg:- ord(z)=122 and ord(a)=97 so 122-97+1=26
                total+=postion*reverse_deg
                postion+=1
        return total