class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_to_words = {}
        for word in strs:
            counts = [(letter, word.count(letter)) for letter in word]
            letters = frozenset(counts)
            if letters in letters_to_words:
                letters_to_words[letters].append(word)
            else:
                letters_to_words[letters] = [word]

        return letters_to_words.values()