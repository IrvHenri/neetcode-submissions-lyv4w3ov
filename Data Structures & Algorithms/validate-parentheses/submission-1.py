class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')','[':']','{':'}'}

        # scan string
            # add opening brackets to stack
            # if its a closing bracked, check if top matches
            #  if it does then pop off the stack
        for char in s:
            if char in brackets:
                stack.append(char)
            else:
    
                if stack and brackets.get(stack[-1]) == char:
                    stack.pop()
                else:
                    return False



        print(stack)
        return len(stack) == 0

        