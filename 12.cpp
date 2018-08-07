class Solution {
public:
    inline void addSymbol(string& s, int& num, int value, const string& symbol) {
        int numRepeat = num / value; 
        if (numRepeat != 0) {
            for (int i = 0; i < numRepeat; i++) {
               s += symbol;
            }
            
            num %= value;
        }
    }
    
    const string SYMBOLS[13] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    const int VALUES[13] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    const int NUM_SYMBOLS = 13;
    string intToRoman(int num) {
        string result ="";
        for (int i = 0; i < NUM_SYMBOLS; i++) {
            addSymbol(result, num, VALUES[i], SYMBOLS[i]);
        }
        return result;
    }
};
