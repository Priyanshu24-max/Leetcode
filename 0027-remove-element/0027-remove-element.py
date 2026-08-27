class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        new=nums.copy()
        nums.clear()
        for x in new:
            if(x!=val):
                nums.append(x)
                i+=1
        return i        