class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if bills[0] != 5:
            return False
        fives = 0
        tens = 0
        twenties = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                fives += 1
            
            elif bills[i] == 10:
                fives -= 1
                tens += 1
                if fives < 0:
                    return False
            else:
                twenties += 1
                if tens > 0:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
                if fives < 0 or tens < 0:
                    return False
        return True
