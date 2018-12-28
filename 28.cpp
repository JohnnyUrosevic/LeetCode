class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle == "") return 0;
        if (needle.size() > haystack.size()) return -1;
        
        for (int i = 0; i < haystack.size() - needle.size() + 1; i++) {
            if (haystack[i] == needle[0]) {
                for (int j = 1; j < needle.size(); j++) {
                    if (haystack[i+j] != needle[j]) {
                        goto main_loop;
                    }
                }
                return i;
            }
            
            main_loop: ;
        }
        
        return -1;
    }
};
