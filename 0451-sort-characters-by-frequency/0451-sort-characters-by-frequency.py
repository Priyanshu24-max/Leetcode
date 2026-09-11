class Solution:
    def frequencySort(self, s: str) -> str:
        count={}

        for x in s:
            count[x]=count.get(x,0)+1
        result=sorted(count.items(),key=itemgetter(1),reverse=True) #sort the dict in decending order according to the value and itemgetter(1) means take index 1 of each tuple, i.e. take the frequency.
        new=[] #to store final string

        for key,value in result:
            new.append(key*value) #append key*value means if key:e and value:2 then append "ee"
        return "".join(new)
        