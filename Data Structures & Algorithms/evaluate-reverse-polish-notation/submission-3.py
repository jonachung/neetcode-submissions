class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # have a stack []
        # go through the tokens
        # if is number, add it to the stack
        # if is operator, take out two numbers from the stack
        #   -> do operation for those two numbers, get result, add back in stack
        # after going through tokens, get number from stack and that is answer

        stack = []
        operators = set(["*", "-", "+", "/"])
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                operator = tokens[i]
                total = 0
                if operator == "*":
                    total = stack.pop() * stack.pop()
                elif operator == "-":
                    num1, num2 = stack.pop(), stack.pop()
                    total = num2 - num1
                elif operator == "+":
                    total = stack.pop() + stack.pop()
                else:
                    num1, num2 = stack.pop(), stack.pop()
                    total = int(num2 / num1)
                stack.append(total)

        return stack[0]

                    