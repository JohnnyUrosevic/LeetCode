class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        if (board.empty()) return 0;
        
        int count = 0;
        int cols = board[0].size();
        int rows = board.size();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == 'X') {
                    if ((j == 0 || board[i][j-1] == '.') && (i == 0 || board[i-1][j] == '.')) {
                        count++;
                    }
                }
            }
        }
        
        return count;
    }
};
