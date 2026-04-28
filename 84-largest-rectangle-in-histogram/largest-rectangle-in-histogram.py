class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        n = len(heights)
        max_area = 0

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, heights[idx] * width)
            stack.append(i)

        while stack:
            idx = stack.pop()
            width = n - stack[-1] - 1 if stack else n
            max_area = max(max_area, heights[idx] * width)

        return max_area