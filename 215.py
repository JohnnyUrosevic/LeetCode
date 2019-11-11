from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heappush(h, -num)
        
        for i in range(k):
            min_val = heappop(h)
        
        return -min_val