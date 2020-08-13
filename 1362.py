class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        divisors_1 = self.findDivisors(num+1)
        divisors_2 = self.findDivisors(num+2)
        
        if abs(divisors_1[0] - divisors_1[1]) <= abs(divisors_2[0] - divisors_2[1]):
            return divisors_1
        else:
            return divisors_2
    
    def findDivisors(self, num: int) -> List[int]:
        root = math.floor(math.sqrt(num))
        
        for n in range(root, 0, -1):
            if num % n == 0:
                return [n, num // n]
