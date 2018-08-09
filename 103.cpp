class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        
        if (root == nullptr) {
            return result;
        }
        
        
        stack<TreeNode*> toAdd[2];
        int i = 0;
        
        toAdd[i].push(root);
        
        while (!toAdd[i].empty()) {
            vector<int> row;
            
            while (!toAdd[i].empty()) {
                TreeNode* curr = toAdd[i].top();
                toAdd[i].pop();
                
                row.push_back(curr->val);
                
                if(i) {
                    if (curr->right != nullptr) toAdd[!i].push(curr->right);
                    if (curr->left  != nullptr) toAdd[!i].push(curr->left);
                }
                else {
                    if (curr->left  != nullptr) toAdd[!i].push(curr->left);
                    if (curr->right != nullptr) toAdd[!i].push(curr->right);
                }
            }
            
            result.push_back(row);
            i = !i; //swap stacks
        }
        
        return result;
    }
};
