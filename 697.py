from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        degree = max([n for _, n in freq.items()])
        if degree == 1:
            return 1

        freq_nums = [item for item, n in freq.items() if n == degree]

        min_len = float('inf')
        for num in freq_nums:
            first = nums.index(num)
            last = list(reversed(nums)).index(num)
            
            min_len = min(min_len, last-first+1)

        return int(min_len)

