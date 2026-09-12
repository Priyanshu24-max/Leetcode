class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[int(i) for i in range(1,n+1)]

        i=0

        while i<len(answer):
            if answer[i]%3==0 and answer[i]%5==0:
                answer[i]="FizzBuzz"
            elif answer[i]%3==0:
                answer[i]="Fizz" 
            elif answer[i]%5==0:
                answer[i]="Buzz"

            i+=1  
        str_list=[str(x) for x in answer]      
        return str_list
        