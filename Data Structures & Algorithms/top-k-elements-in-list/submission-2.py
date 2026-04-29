import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        heap = []

        total = [0] * k

        for a, b in count.items():

            heapq.heappush(heap, (-b, a))

        for i in range(k):
            total[i] = heapq.heappop(heap)[1]

        return total


        

        


        