class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_1=Counter(s) #count freq of each element of s
        counter_2=Counter(t) #count freq of each element of t

        diff_1=counter_1-counter_2 #char in string 1 but not in string 2
        diff_2=counter_2-counter_1 #char in string 2 but not in string 1

        uncommon_word=diff_1+diff_2 #combining unique char
        result="".join(uncommon_word)

        return result