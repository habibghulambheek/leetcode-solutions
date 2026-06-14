import heapq
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        distances = [(-(aliceValues[i] + bobValues[i]), i) for i in range(n)]

        bob_score = 0
        alice_score = 0
        heapq.heapify(distances)
        turn = True
        while distances:
            x, i = heapq.heappop(distances)
            if turn:
                alice_score += aliceValues[i]
            else:
                bob_score += bobValues[i]
            turn = not turn
        if alice_score > bob_score:
            return 1
        elif bob_score > alice_score:
            return -1 
        return 0

        # [1,2,6,3]
        # a = 17
        # b = 16