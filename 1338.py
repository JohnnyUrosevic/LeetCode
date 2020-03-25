class Solution:
    from heapq import heappop, heappush, heapify
    from collections import defaultdict
    def minSetSize(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        
        for num in arr:
            counts[num] += 1
        
        heap = [-c for c in counts.values()]
        heapify(heap)
        
        l = len(arr)
        target = len(arr) / 2
        size = 0

        while l > target:
            size += 1
            l += heappop(heap)
            
        return size