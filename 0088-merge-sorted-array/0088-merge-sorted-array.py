class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        while(i<len(nums2)):
            nums1[m]=nums2[i]
            i+=1
            m+=1
        nums1.sort()  