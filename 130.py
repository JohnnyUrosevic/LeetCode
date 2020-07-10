class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        for i in range(0, len(board)):
            for j in [0, len(board[0])-1]:
                if board[i][j] == "O":
                    self.DFS(i, j, board)
        
        for j in range(0, len(board[0])):
            for i in [0, len(board)-1]:
                if board[i][j] == "O":
                    self.DFS(i, j, board)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "B":
                    board[i][j] = "O"
        
    def DFS(self, i, j, board):
        dirs = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
        ]
        
        board[i][j] = "B"
        
        
        for dir in dirs:
            di = i + dir[0]
            dj = j + dir[1]
            
            if di < 0 or dj < 0 or di == len(board) or dj == len(board[0]):
                continue
            
            if board[di][dj] == "O":
                path = self.DFS(di, dj, board)
