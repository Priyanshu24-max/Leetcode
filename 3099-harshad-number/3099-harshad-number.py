class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        original=x
        digit=[]

        while(original>0):
            digit.append(original%10)
            original=original//10

        add=sum(digit)

        if(x%add==0):
            return add
        else:
            return -1    