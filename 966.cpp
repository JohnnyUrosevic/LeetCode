class Solution {
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        unordered_set<string> words;
        unordered_map<string, string> lowerToCorrect;
        unordered_map<string, int> lowerToIndex;
        
        string vowels = "aeiou";
        
        for (int i = 0; i < wordlist.size(); i++) {
            string word = wordlist[i];
            
            words.insert(word);
            
            string lowerword = word;
            transform(lowerword.begin(), lowerword.end(), lowerword.begin(), ::tolower);
            if (lowerToCorrect.find(lowerword) != lowerToCorrect.end()) continue;
            
            lowerToCorrect[lowerword] = word;
            lowerToIndex[lowerword] = i;
        }
        
        vector<string> result;
        
        for (string query : queries) {
            if (words.find(query) != words.end()) {
                result.push_back(query);
                continue;
            }
            
            transform(query.begin(), query.end(), query.begin(), ::tolower);
            
            if (lowerToCorrect.find(query) != lowerToCorrect.end()) {
                result.push_back(lowerToCorrect[query]);
                continue;
            }
            
            for (int i = 0; i < query.size(); i++) {
                if (vowels.find(query[i]) != string::npos) {
                    string correctWord = "";
                    int minIndex = 5000;
                    for (char vowel : vowels) {
                        string tempWord = query;
                        tempWord[i] = vowel;
                        auto it = lowerToIndex.find(tempWord);
                        if (it != lowerToIndex.end()) {
                            if(it->second < minIndex) {
                                minIndex = it->second;
                                correctWord = lowerToCorrect[tempWord];
                            }
                        }
                    }
                    
                    //check for multiple vowels ugh
                }
            }
            

            
            result.push_back(""); //no match
        }
        
        return result;
    }
};
