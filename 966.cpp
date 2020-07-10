class Solution {
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        unordered_set<string> raw;
        unordered_map<string, string> dictionary;
        unordered_map<string, int> priority;
        
        for (size_t i = 0; i < wordlist.size(); i++) {
            auto word = wordlist[i];
            raw.insert(word);
            
            string lower = "";
            for (char c : word) {
                lower += tolower(c); 
            }
            
            if (dictionary.find(lower) == dictionary.end()) {
                dictionary[lower] = word;
                priority[word] = i;
            }
        }
        
        vector<string> result;
        
        
        
        for (auto word : queries) {
            if (raw.find(word) != raw.end()) {
                result.push_back(word);
                continue;
            }
            
            string lower = "";
            for (char c : word) {
                lower += tolower(c); 
            }

            if (dictionary.find(lower) != dictionary.end()) {
                result.push_back(dictionary[lower]);
                continue;
            }
            
            
            auto possibilities = replace_vowels(lower);
            
            vector<string> matches;
            for (auto possibility : possibilities) {
                if (dictionary.find(possibility) != dictionary.end()) {
                    matches.push_back(dictionary[possibility]);
                }
            } 
            
            int min = INT_MAX;
            string min_word = "";
            if (matches.size()) {
                for (auto match : matches) {
                    auto p = priority[match];
                    if (p < min) {
                        min = p;
                        min_word = match;
                    }
                }
            }
            
            result.push_back(min_word);
        }
        
        return result;
    }
    
    vector<string> replace_vowels(string word) {
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        
        vector<string> possibilities;
        for (size_t i = 0; i < word.size(); i++) {
            if (vowels.find(word[i]) != vowels.end()) {
                vector<string> subs = replace_vowels(word.substr(i+1));
                string pre = word.substr(0, i);
                for (auto v : vowels) {
                    for (auto sub : subs) {
                        possibilities.push_back(pre + v + sub);
                    }
                }
            }
        }
        
        if (possibilities.size() == 0) {
            possibilities.push_back(word);
        }
        return possibilities;
    } 
};
