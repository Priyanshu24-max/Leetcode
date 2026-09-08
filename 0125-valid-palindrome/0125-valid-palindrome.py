class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(char for char in s if char.isalnum()) #check if there is any space or punctuation and remove it
        s=s.lower() #convert all the letter to lower case
        if (s==s[::-1]):
            return True #if palindrome return True 
        else:
            return False #else False