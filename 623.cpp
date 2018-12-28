/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if (d == 1) {
            TreeNode* node = new TreeNode(v);
            node->left = root;
            
            return node;
        }
        
        queue<TreeNode*> level;
        level.push(root);
                
        long long unsigned int nodesToSkip = 0;
        
        for (int i = 0; i < d - 2; i++) {
            nodesToSkip = nodesToSkip << 1;
            nodesToSkip++;
        }
        
        cout << nodesToSkip << endl;
        
        int prevN = pow(2, d - 2);
        
        TreeNode* curr;
        for (int i = 0; i < nodesToSkip; i++) {
            curr = level.front();
            level.pop();
            
            if (curr == nullptr) {
                level.push(nullptr);
                level.push(nullptr);
                continue;
            }
            
            level.push(curr->left);
            level.push(curr->right);
        }
        
        for (int i = 0; i < prevN; i++) {
            curr = level.front();
            level.pop();
                        
            if (curr == nullptr) {
                continue;
            }
            
            TreeNode* tempLeft = curr->left;
            TreeNode* tempRight = curr->right;
            
            curr->left = new TreeNode(v);
            curr->right = new TreeNode(v);
            
            curr->left->left = tempLeft;
            curr->right->right = tempRight;
        }        
        
        return root;
    }
};
