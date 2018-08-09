class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        
        if (root == nullptr) {
            return result;
        }
        
        queue<TreeNode*> toPrint[2];
        
        int i = 0;
        toPrint[i].push(root);

        while( !(toPrint[0].empty() && toPrint[1].empty()) ) {
            vector<int> row;
            
            while(!toPrint[i].empty()) {
                TreeNode* curr = toPrint[i].front();
                toPrint[i].pop();
                
                row.push_back(curr->val);
                
                //put next level in a different queue
                if (curr->left)  toPrint[!i].push(curr->left);
                if (curr->right) toPrint[!i].push(curr->right);
            }
            
            result.push_back(row); 
            i = !i; //swap queues
        }
        return result;
    }
};
