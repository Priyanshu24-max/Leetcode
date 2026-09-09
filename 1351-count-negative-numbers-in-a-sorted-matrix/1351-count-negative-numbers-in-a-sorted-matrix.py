class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        flat_arr=[item for row in grid for item in row] #convert the 2D array into 1D

        count=0

        for x in flat_arr:
            if x<0:
                count+=1
        return count