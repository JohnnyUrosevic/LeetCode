class Solution {
public:
    string largestNumber(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        vector<string> numsToString;
        
        for (int n : nums) {
            numsToString.push_back(to_string(n));
        }
        
        auto compare = [](string const& a, string const& b){ 
            return a + b > b + a;
        };
        
        sort(numsToString.begin(), numsToString.end(), compare);
        string result = "";
        
        for (string num : numsToString) {
            result += num;
        }
        
        if (result[0] == '0') {
            return "0";
        }
        
        return result;
    }    
};
