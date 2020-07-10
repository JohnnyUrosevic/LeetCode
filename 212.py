class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []
        
        trie = {}
        
        for word in words:
            curr = trie
            for letter in word:
                if letter not in curr:
                    curr[letter] = {}
                curr = curr[letter]
            curr["!"] = {}
        
        curr = trie
        
        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (letter := board[i][j]) in trie:
                    result = self.dfs((i, j), board, trie[board[i][j]], letter, set(), result)
                
        return result
                
    def dfs(self, point, board, trie, word, visited, result):
        i, j = point
        
        dirs = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
        ]
        visited.add((i, j))
        
        for dir in dirs:
            di = i + dir[0]
            dj = j + dir[1]
            
            if (di, dj) in visited or di < 0 or dj < 0 \
                or di == len(board) or dj == len(board[0]):
                continue
            
            letter = board[di][dj]
            if letter in trie:
                result = self.dfs((di, dj), board, trie[letter], word + letter, visited.copy(), result)
                
        if "!" in trie and word not in result:
            result.append(word)
        
        return result
