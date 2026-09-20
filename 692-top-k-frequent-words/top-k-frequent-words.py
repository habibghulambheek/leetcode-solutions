class Reverse:
    def __init__(self, word):
        self.word = word
    def __lt__(self, other):
        return self.word > other.word
class Solution(object):
    def topKFrequent(self, words, k):
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        heap = []
        for word, count in freq.items():
            heapq.heappush(heap, (count, Reverse(word)))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1].word)
        return res[::-1]