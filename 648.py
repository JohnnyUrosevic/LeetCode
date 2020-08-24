class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for prefix in dictionary:
            curr = trie
            for letter in prefix:
                if letter not in curr:
                    curr[letter] = {}
                curr = curr[letter]
            curr["!"] = True
        
        result = []
        for word in sentence.split(" "):
            curr = trie
            add_word = True
            prefix = ""
            
            for letter in word:
                prefix += letter
                if letter not in curr:
                    break
                curr = curr[letter]
                if "!" in curr:
                    result.append(prefix)
                    add_word = False
                    break
            
            if add_word:
                result.append(word)
        
        return " ".join(result)
