class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            seen.add(n)
            m = n
            sum_digits = 0
            while m != 0:
                sum_digits += (m % 10) ** 2
                m //= 10
            
            n = sum_digits
            if n in seen:
                return False
                
        return True