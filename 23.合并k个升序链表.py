#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # not overtime 
        # time complex O(lgn) 
        # space complex o(n)
        import heapq
        if not lists:
            return None
        arr = []
        for l in lists:
            if not l:
                continue
            while l:
                heapq.heappush(arr, l.val)
                l = l.next
        # arr.sort()
        ans = ListNode()
        head = ans
        while arr:
            node = ListNode(heapq.heappop(arr))
            head.next = node
            head = head.next
        return ans.next

# @lc code=end

