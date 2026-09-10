class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[] #to store all postive numbers present in nums
        neg=[] #to store all negative numbers present in nums
        result=[] #to store the final resultant array

        for x in nums:
            if x>0: #if x is postive append in pos array
                pos.append(x)
            else:
                neg.append(x) #else in neg array
        for x in range(len(pos)):
            result.append(pos[x]) #as we want first element to be postive we appended postive value first
            result.append(neg[x])
        return result
