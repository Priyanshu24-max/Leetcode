class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        sort_nums1=sorted(nums1) 
        sort_nums2=sorted(nums2)

        i=0
        j=0

        result=[]
        while i<len(sort_nums1) and j<len(sort_nums2):
            if sort_nums1[i]<sort_nums2[j]: #if the element in nums1 is smaller the element in nums2 then increase the pointer of nums1 by 1
                i+=1
            elif sort_nums1[i]>sort_nums2[j]:#if the element in nums2 is smaller the element in nums1 then increase the pointer of nums2 by 1
                j+=1
            else:
                result.append(sort_nums1[i]) #if both element are equal then append it to result
                i+=1
                j+=1
        return result

