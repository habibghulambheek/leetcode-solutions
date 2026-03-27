class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(arr)
        max_val = -1
        for i in range(n-1,-1,-1):
            value = arr[i]
            # print(max_val)

            arr[i] = max_val
            max_val = max(value, max_val)
        return arr