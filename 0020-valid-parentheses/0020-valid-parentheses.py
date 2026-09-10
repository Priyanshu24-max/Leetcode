class Solution:
    def isValid(self, s: str) -> bool:
        stack=[] #keep track of the opening parentheses as we encounter them in the string

        pairs={")":"(","}":"{","]":"["} # in pairs array we are adding first ")" and then "(" because if we push it in stack it will make it () and if we add "(" first then ")" then it will result in )( which result in non valid parentheses 

        for char in s:
            if char in pairs: #checks if the current char is a closing parenthesis by seeing if it exists in the pairs dictionarys 

                if not stack or stack[-1]!=pairs[char]: #check if the stack is empty or if the top element of string doesnot matches the opening parentheses for the closing parentheses
                    return False

                stack.pop() #if the parentheses match

            else:
                stack.append(char) # if char not in stack then append it

        return len(stack)==0 #if the stack gets empty means all were Valid Parentheses
