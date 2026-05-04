class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        result = 0

        for i in range(len(tokens)):

            if tokens[i] not in {'+', '-', '*', '/'}:
                stack.append(int(tokens[i]))

            else:
                right = int(stack.pop())
                left = int(stack.pop())

                if tokens[i] == '+':
                    result = left + right
                elif tokens[i] == '-':
                    result = left - right
                elif tokens[i] == '*':
                    result = left * right
                else:
                    result = left / right   
                stack.append(result)

        return int(stack.pop())

        