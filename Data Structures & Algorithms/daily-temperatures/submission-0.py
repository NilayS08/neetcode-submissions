class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        output = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                old_index = stack.pop()
                output[old_index] = i - old_index
            stack.append(i)
        return output