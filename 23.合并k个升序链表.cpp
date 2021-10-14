/*
 * @lc app=leetcode.cn id=23 lang=cpp
 *
 * [23] 合并K个升序链表
 */

// @lc code=start
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode dummy(0);
        ListNode *tail = &dummy;

        auto comp = [](ListNode* a, ListNode* b) {return a->val > b->val; };
        priority_queue<ListNode*, vector<ListNode*>, decltype(comp)> q(comp);

        for (ListNode* list: lists) {
            if (list) q.push(list);
        }
        while (!q.empty()) {
            tail->next = q.top();
            q.pop();
            tail = tail->next;
            if (tail->next) q.push(tail->next);
        }
        return dummy.next;
    }
};
// @lc code=end

