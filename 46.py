class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        if len(nums) == 1:
            return [nums]

        result = []
        for i in range(len(nums)):
            permutation = nums.copy()
            permutation[0], permutation[i] = permutation[i], permutation[0]
            result += [permutation[:1] + x for x in self.permute(permutation[1:])]
            
        return result
