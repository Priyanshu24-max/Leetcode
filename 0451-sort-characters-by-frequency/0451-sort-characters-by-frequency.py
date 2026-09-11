class Solution:
    def frequencySort(self, s: str) -> str:
        count={}

        for x in s:
            count[x]=count.get(x,0)+1
        result=dict(sorted(count.items(),key=itemgetter(1),reverse=True)) #sort the dict in decending order according to the value
        new=[] #to store final string

        for key,value in result.items():
            new.append(key*value) #append key*value means if key:e and value:2 then append "ee"
        return "".join(new)
        