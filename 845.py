class Solution:
    def longestMountain(self, A: List[int]) -> int:
        current_len = 1
        max_len = 1
        
        increasing = True
        
        for i in range(1, len(A)):
            if A[i - 1] < A[i] and increasing:
                current_len += 1
            elif A[i - 1] > A[i] and increasing and current_len > 1:
                current_len += 1
                increasing = False
            elif A[i - 1] > A[i] and not increasing:
                current_len += 1
            else:
                max_len = max(current_len, max_len)
                if A[i - 1] < A[i] and not increasing:
                    current_len = 2
                else:
                    current_len = 1
                increasing = True
                
        if not increasing:
            max_len = max(current_len, max_len)
            
        return max_len if max_len >= 3 else 0