//Also works for 117
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (root == nullptr) return;
        queue<TreeLinkNode*> level[2];
        int i = 0;
        
        level[i].push(root);
        
        while(!level[i].empty()) {
            TreeLinkNode* prev;
            TreeLinkNode* curr;
            while(!level[i].empty()) {
                curr = level[i].front();
                level[i].pop();
                
                if (curr->left) level[!i].push(curr->left);
                if (curr->right) level[!i].push(curr->right);
                
                if (prev) prev->next = curr;
                
                prev = curr;
            }
            prev->next = nullptr;
            prev = nullptr;
            i = !i;
        }
    }
};
