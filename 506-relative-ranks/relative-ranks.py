import heapq
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = len(score)
        heap = []
        placements =  [(-score[i], i) for i in range(n) ]
        heapq.heapify(placements)
        placement = 1
        while placements:
            
            pair = heapq.heappop(placements)
            # print(pair, placement)
            if placement == 1: 
                score[pair[1]]  = "Gold Medal"  
            elif placement == 2:
                score[pair[1]]  = "Silver Medal"
            elif placement ==  3:
                score[pair[1]] = "Bronze Medal"
            else:
                score[pair[1]] = str(placement)
            placement += 1
        return score