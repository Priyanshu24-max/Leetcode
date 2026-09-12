class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        vol=length*width*height

        ans=set() # so no duplicate stores
                
        bulk=vol>=10**9 or length>=10**4 or width>=10**4 or height>=10**4
        if (bulk):
            ans.add("Bulky")
        if (mass>=100):
            ans.add("Heavy")

        if len(ans)==2: # if length is 2 means both heavy and bulky is present
            return "Both"
        elif "Heavy" in ans:
            return "Heavy"
        elif "Bulky" in ans:
            return "Bulky"  
        return "Neither"   
        