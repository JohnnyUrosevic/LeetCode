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
    bool isValidBST(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        
        vector<int> vals;
        inorder(root, vals);
        
        int prev = vals[0];
        for (int i = 1; i < vals.size(); i++) {
            if (vals[i] <= prev) {
                return false;
            }
            
            prev = vals[i];
        }
        
        return true;
    }
    
    void inorder(TreeNode* root, vector<int>& vals) {
        if (root == nullptr) {
            return;
        }
        
        inorder(root->left, vals);
        vals.push_back(root->val);
        inorder(root->right, vals);
    }
};
