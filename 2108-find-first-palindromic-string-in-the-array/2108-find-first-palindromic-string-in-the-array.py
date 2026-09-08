class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words: # iterate every word
            if (word==word[::-1]): #check if the reverse of that word is equal to the orginal
                return word #if yes return that word 
        return "" # if not return empty string