class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=int("".join(map(str, digits)))
        a+=1
        digits=(list(str(a)))
        digits=[int(x) for x in digits]
        return (digits)