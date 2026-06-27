class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapq.heapify(heap)
        while k != 0:
            heapq.heapreplace(heap,-math.floor((-heap[0])**(0.5)))
            k -= 1
        return -sum(heap)