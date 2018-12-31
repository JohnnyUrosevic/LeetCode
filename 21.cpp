static int fast = []() {ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0); return 0; }();
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;
        
        ListNode* root;
        
        if (l1->val < l2->val) {
            root = new ListNode(l1->val);
            l1 = l1->next;
        }
        else {
            root = new ListNode(l2->val);
            l2 = l2->next;
        }
        
        ListNode* curr = root;
        
        while (l1 && l2) {
            if (l1->val < l2->val) {
                curr->next = new ListNode(l1->val);
                l1 = l1->next;
            }
            else {
                curr->next = new ListNode(l2->val);
                l2 = l2->next;
            }

            curr = curr->next;
        }
        
        if (!l1) {
            curr->next = l2;
        }
        else {
            curr->next = l1;
        }
        
        return root;
    }
};
