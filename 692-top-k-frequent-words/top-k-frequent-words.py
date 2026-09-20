from collections import Counter
import heapq
class Item:
    def __init__(self,count, word):
        self.count = count
        self.word  = word
        # print(word)
    def __lt__(self, other):
        if self.count != other.count:
            return self.count < other.count
        return self.word > other.word
    def __repr__(self):
        return self.word + ":" + str(self.count)
    
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counts =  Counter(words)
        min_heap = []
        for word, count in counts.items():
            item = Item(count, word)
            heapq.heappush(min_heap, item)
            if len(min_heap) > k:
                  heapq.heappop(min_heap)

        ans = []
        while min_heap:
            ans.insert(0,heapq.heappop(min_heap).word)
        return ans

