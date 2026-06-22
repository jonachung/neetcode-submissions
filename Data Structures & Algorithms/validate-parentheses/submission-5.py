class Solution:
    def isValid(self, s: str) -> bool:
        # loop through characters in s
        # put 'left' brackets in a stack
        # if get a 'right' bracket, check if stack[-1] is respective left bracket
        # if so, pop from stack
        # if not, add right bracket in

        # after looping, if stack is not empty return false else return true

        stack = []
        for parenthesis in s:
            if parenthesis == '(' or parenthesis == '{' or parenthesis == '[':
                stack.append(parenthesis)
            else:
                if (len(stack) != 0) and ((parenthesis == ')' and stack[-1] == '(') or (parenthesis == '}' and stack[-1] == '{') or (parenthesis == ']' and stack[-1] == '[')):
                    stack.pop()
                else:
                    stack.append(parenthesis)

        if len(stack) == 0:
            return True
        return False
