class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # gas = [3,2,3,4,5], cost = [7,0,3,1,2]
        # actual = [-7,2,0,3,3]
        if sum(gas) < sum(cost) :
            return -1 
        running_cost = gas[0] - cost[0]
        start = 0
        for i in range(1,len(gas)):    
            if running_cost < 0:
                start = i
                running_cost = 0
            running_cost += gas[i] - cost[i]
            # print(running_cost, start)
        return start