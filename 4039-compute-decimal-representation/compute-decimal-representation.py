class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        
        multiplier = 1
        ans = []
        while n != 0:
            number = n % 10
            number *= multiplier
            if number != 0:
                ans.append(number)
            multiplier *= 10
            n //= 10
        
        return ans[::-1]