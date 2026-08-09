class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        import string 

        word=list(word)
        char=[char for char in word if char.isupper()]

        size=len(word)
        chr_size=len(char)

        if (size==chr_size or chr_size==0):
            return (True)
        elif (chr_size==1):
            indexs=[word.index(x) for x in char if x in word]
            if (indexs[0]==0):
                return (True)
            else:
                return (False)
        else:
            return (False)