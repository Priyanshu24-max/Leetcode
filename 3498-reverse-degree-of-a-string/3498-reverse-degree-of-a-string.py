class Solution:
    def reverseDegree(self, s: str) -> int:
        s=list(s)
        lower_alpha=[chr(x) for x in range(ord('a'),ord('z')+1)] #to store all alphabet in lowercase
        lower_alpha=sorted(lower_alpha,reverse=True) #reverse the array

        sums=[] #store the product of Index in String and Index in Reversed Alphabet
        i=1
        
        for x in s:
            if x in lower_alpha:
                sums.append(i*(lower_alpha.index(x)+1))
                i+=1
        return sum(sums)      