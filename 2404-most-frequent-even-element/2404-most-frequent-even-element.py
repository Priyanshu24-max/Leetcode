class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count={} #to keep the key as numbers and value as number of time key number appears

        for x in nums:
            if x%2==0: #if number is divisible by 2 then only store it in count
                count[x]=count.get(x,0)+1 
        if len(count)==0: 
            return -1

        max_freq = max(count.values()) #store the max frequence value
        max_key=[key for key,value in count.items() if value==max_freq] #if the value is equal to max_freq then store it in array   

        return min(max_key)  

        