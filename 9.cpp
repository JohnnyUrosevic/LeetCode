class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        
        int sum = 0;  
        int originalX = x;
        while (x != 0) {
            if ((sum * 10) % 10 != 0) {
                return false;
            } 
            
            sum *= 10;
            
            sum += x % 10;
            
            x /= 10;
        }
        return sum == originalX;
    }
};
