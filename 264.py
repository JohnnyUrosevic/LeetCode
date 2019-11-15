from heapq import heappush, heappop
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = set(heap)

        i = 1
        while i < n - 1:
            top = heap[0]
            heappop(heap)

            ugly = top * 2
            if ugly not in seen:
                heappush(heap, ugly)
                seen.add(ugly)

            ugly = top * 3
            if ugly not in seen:
                heappush(heap, ugly)
                seen.add(ugly)

            ugly = top * 5
            if ugly not in seen:
                heappush(heap, ugly)
                seen.add(ugly)

            i+=1
        
        return heap[0]