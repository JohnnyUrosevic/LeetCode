from heapq import heappush, heappop, heappushpop
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        
        for p in points:
            if len(heap) == K:
                heappushpop(heap, (-sqrt(p[0] ** 2 + p[1] ** 2), p))
            else:
                heappush(heap, (-sqrt(p[0] ** 2 + p[1] ** 2), p))
                
        return [x[1] for x in heap]
