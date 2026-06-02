class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result array is 0 for all temperatures
        # stack to store (temp, index)
        # loop through temperatures
        # if temp < temp in top of stack -> add to stack
        # if temp > top of stack
        # pop from stack, get index diff, replace 0 with index diff for that index that is popped in result array

        result = [0 for _ in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures)):

            while stack and stack[-1][0] < temperatures[i]:
                recentTemp, index = stack.pop()
                result[index] = i - index

            stack.append((temperatures[i], i))

        return result