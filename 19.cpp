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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* before = nullptr;
        ListNode* target = head;
        ListNode* ptr = head;
        for (int i = 1; i < n; i++) {
            ptr = ptr->next;
        }
        
        while (ptr->next != nullptr) {
            ptr = ptr->next;
            if (before == nullptr) {
                before = head;
            }
            else {
                before = before->next;
            }
            target = target->next;
        }
        
        if (before == nullptr) {
            head = target->next;
        }
        else {
            before->next = target->next;
        }
        
        delete target;
        
        return head;
    }
};
