class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        strs=s+s
        if (len(s)!=len(goal)):
            return (False)
        elif goal in strs:
            return (True)
        else:
            return (False)        