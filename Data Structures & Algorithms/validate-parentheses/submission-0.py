class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        dic = {'(' : ')', '{' : '}', '[' : ']'}

        for i in range(len(s)):

            if dic.get(s[i]) is not None:
                stack.append(dic.get(s[i]))
            else:
                if len(stack) >= 1:
                    popped = stack.pop()
                    if s[i] != popped:
                        return False
                else:
                    return False 
            
        if len(stack) == 0:
            return True 
        return False 