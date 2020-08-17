/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (!head) {
            return nullptr;
        }
        if (!head->next) {
            return head;
        }
        
        ListNode* odd_head = head;
        ListNode* even_head = even_head = head->next;

        
        ListNode* odd = odd_head;
        ListNode* even = even_head;
        
        ListNode* curr = nullptr;
        curr = head->next->next;
        
        bool curr_odd = true;
        while (curr) {
            ListNode* next = curr->next;
            if (curr_odd) {
                odd->next = curr; 
                odd = odd->next;
            } 
            else {
                even->next = curr;
                even = even->next;
            }
            
            curr = next;
            curr_odd = !curr_odd;
        }
        
        odd->next = even_head;
        even->next = nullptr;
        
        return odd_head;
    }
};
