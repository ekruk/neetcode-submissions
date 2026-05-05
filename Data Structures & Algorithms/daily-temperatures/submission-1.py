class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        new_temp = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while len(stack) >= 1 and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                new_temp[index] = i - index 
            stack.append(i)

        return new_temp


        
        