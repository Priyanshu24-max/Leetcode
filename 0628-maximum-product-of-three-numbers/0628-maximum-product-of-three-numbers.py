class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1=max2=max3=float(-inf) #to store top three maximum value
        min1=min2=float(inf) #to store two minimum value

        for x in nums:
            if x>max1:
                max3=max2
                max2=max1
                max1=x
            elif x>max2:
                max3=max2
                max2=x
            elif x>max3:
                max3=x
            
            if x<min1:
                min2=min1
                min1=x
            elif x<min2:
                min2=x
        return max(min1*min2*max1,max1*max2*max3) #first taking two small and one large value as product of two neg is postive and if we multiply it by largest value the product will be max and then multiplying top three values and comparing the max of them
        