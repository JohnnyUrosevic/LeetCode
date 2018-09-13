class Solution {
public:
    int totalNQueens(int n) {
        stack<vector<int>> possibilities;
        int validSolutions = 0;
        
        for (int i = 1; i <= n; i++) {
            vector<int> queens(n);
            queens.push_back(i);
            possibilities.push(queens);
        }
        
        while (!possibilities.empty()) {
            auto queens = possibilities.top();
            possibilities.pop();
            
            if (queens.size() == n) {
                validSolutions++;
                continue;
            }
            
            for (int i = 1; i <= n; i++) {
                if (std::find(queens.begin(), queens.end(), i) != queens.end()) {
                    queens.push_back(i);
                    possibilities.push(queens);
                    queens.pop_back();
                }
            }
        }
        
        return validSolutions;
    }
};
