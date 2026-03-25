class Solution(object):
   def dailyTemperatures(self, temperatures):
    n = len(temperatures)
    ans = [0] * n
    stack = []  # stores indices

    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            idx = stack.pop()
            ans[idx] = i - idx  # answer is computed AT pop time
        stack.append(i)

    return ans