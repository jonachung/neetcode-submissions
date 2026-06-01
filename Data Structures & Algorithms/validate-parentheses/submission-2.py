class Solution:
    def isValid(self, s: str) -> bool:
        # create a stack object to hold parenthesis
        # leftParenthesis = [{, [, (]
        # rightParenthesis = [], }, )]

        # loop through s and if left parenthesis, add it to the stack
        # if hit a right parenthesis, peek from stack and check if pair is valid.
        # if yes then remove the left parenthesis from stack
        # if no then add right parenthesis in the stack
        # end of loop -> if stack is empty return True else return False

        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                last = stack[-1]
                if (s[i] == ')' and last == '(') or (s[i] == '}' and last == '{') or (s[i] == ']' and last == '['):
                    stack.pop()
                else:
                    stack.append(s[i])

        print(stack)
        return len(stack) == 0