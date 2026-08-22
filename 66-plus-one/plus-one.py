class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if carry == 0:
                break
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += carry
                carry = 0
        if carry == 1:
            digits.insert(0,1)
        return digits