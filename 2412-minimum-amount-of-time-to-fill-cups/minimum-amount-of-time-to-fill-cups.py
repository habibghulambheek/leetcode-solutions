class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        total_cups = sum(amount)
        formula =  total_cups // 2 + total_cups % 2
        maxx = max(amount)
        return max(maxx, formula)
        