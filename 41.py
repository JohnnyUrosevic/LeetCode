class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        
        #swap items to make array resemble [1, 2, 3, ...]
        i = 0
        while i < size:
            val = nums[i]
            if val <= 0 or val > size:
                i += 1
                continue
            
            if nums[i] == nums[val - 1]:
                i += 1
                continue
                
            nums[i], nums[val - 1] = nums[val - 1], nums[i]
        
        for j in range(size):
            if nums[j] != j + 1:
                return j + 1  
        
        return size + 1
