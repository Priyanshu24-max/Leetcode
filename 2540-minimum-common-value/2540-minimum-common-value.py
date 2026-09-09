class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        new=list(set(nums1)&set(nums2)) # find the common element of both array
        if len(new)==0: #if length of new is zero means no common element then return -1
            return -1
        return min(new) #return the min of new array