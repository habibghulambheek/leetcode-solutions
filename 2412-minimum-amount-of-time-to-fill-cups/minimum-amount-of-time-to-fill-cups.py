class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        ans = 0
        while amount[0] != 0 or amount[1] != 0 or amount[2] != 0:
            idx1, idx2 = None, None
            if amount[0] > amount[1]:
                idx1 = 0
                idx2 = 1
            else:
                idx1 = 1
                idx2 = 0
            if amount[idx1] > amount[2]:
                if amount[2] > amount[idx2]:
                    idx2 = 2
            else:
                idx2 = idx1 
                idx1 = 2
            # print(amount, amount[idx1], amount[idx2])
            amount[idx1] -= 1
            if amount[idx2] != 0:
                amount[idx2] -= 1
            ans += 1
        return ans
        