class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copy=sorted(heights) #created a copy of heights to compare 
        i=0
        count=0 #count how many value at same index doesnot matches

        while(i<len(heights)):
            if(heights[i]!=copy[i]):
                count+=1
                i+=1
            else:
                i+=1
        return count