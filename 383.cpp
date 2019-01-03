static int fast = [](){std::ios_base::sync_with_stdio(false); std::cin.tie(nullptr); return 0;}();

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> available;
        
        for (int i = 0; i < magazine.size(); i++) {
            auto iter = available.find(magazine[i]);
            
            if (iter != available.end()) {
                iter->second++;
            }
            else {
                available.insert(make_pair(magazine[i], 1));
            }
        }
        
        for (int i = 0; i < ransomNote.size(); i++) {
            auto iter = available.find(ransomNote[i]);
            
            if (iter == available.end() || iter->second == 0) {
                return false;
            }
            
            iter->second--;
        }
        
        return true;
    }
};
