class Solution {
public:
    int myAtoi(string str) {
        long int sum = 0;
        bool negative = false;
        bool begin = true;
        
        for (int i = 0; i < str.size(); i++) {
            if (begin) {
                switch(str[i]) {
                    case ' ':
                        continue;
                    case '-':
                        negative=true;
                        //fall through
                    case '+':
                        begin=false;
                        continue;
                    default:
                        begin=false;
                }
            }
            if ((str[i] < '0' || str[i] > '9')) {
                return sum * ((negative) ? -1 : 1);
            }
                        
            sum *= 10;
            sum += (int)(str[i] - '0');
            
            if (sum > INT_MAX) { //overflow
                return ((negative) ? INT_MIN : INT_MAX) + (sum == INT_MAX + 1 && negative && i == str.size() - 1);
            }
        }
                
        return sum * ((negative) ? -1 : 1);
    }
};
