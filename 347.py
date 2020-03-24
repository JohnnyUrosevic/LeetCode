from collections import defaultdict
from heapq import heappush, heappop, heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        
        for element in nums:
            freq[element] += 1
        
        heap = []
        
        for item, count in freq.items():
            heap.append((-count, item))
        
        heapify(heap)
        
        result = []
        for i in range(k):
            _, num = heappop(heap)
            result.append(num)
            
        return result
