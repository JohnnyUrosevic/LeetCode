class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        
        result = ""
        length = max(len(a), len(b))
        a = a[::-1]
        b = b[::-1]
        
        carry = 0
        for i in range(length):
            a_digit = int(a[i]) if i < len(a) else 0
            b_digit = int(b[i]) if i < len(b) else 0
            
            num = a_digit + b_digit + carry
            if num > 1:
                result += str(num % 2);
                carry = 1
            else:
                result += str(num)
                carry = 0
        
        
        if carry == 1:
                result += str(carry)
                
        return result[::-1]
