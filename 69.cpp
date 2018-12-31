class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) return 0;
        long int start = 1;
        long int end = x / 2 + 1;
        
        long int mid;
        
        while (start <= end) {
            mid = (end + start) / 2;
            
            long long int square = mid * mid;
            
            if (square == x) {
                return mid;
            } 
            else if (square < x) {
                start = mid + 1;
            }
            else {
                end = mid - 1;
            }
        }
        
        return start * start > x ? start - 1 : start;
    }
};
