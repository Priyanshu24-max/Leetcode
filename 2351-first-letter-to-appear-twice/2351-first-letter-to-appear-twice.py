class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen=set() # To Store each element which is iterated
        duplicate=list() # Store duplicate elements

        for x in s:
            if x in seen:
                duplicate.append(x) #if the element is present in seen then it means its appearing second time so append it in duplicate list
            else:
                seen.add(x) #if not present in seen then add it
        return "".join(duplicate[0]) # return the first duplicate