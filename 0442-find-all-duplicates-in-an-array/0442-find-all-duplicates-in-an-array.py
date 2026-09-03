class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen=set()
        duplicate=list()

        for i in nums:
            if i in seen:
                duplicate.append(i)
            else:
                seen.add(i)
        return duplicate          