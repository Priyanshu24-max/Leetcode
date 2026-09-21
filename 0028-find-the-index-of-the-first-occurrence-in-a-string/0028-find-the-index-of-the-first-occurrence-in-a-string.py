class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1): #checks every possible starting position where needle can fit inside haystack
            if haystack[i:len(needle)+i]==needle: #check only till the length of needle
                return i #return the first index of first letter of needle in haystack 
        return -1 #other wise return -1
        