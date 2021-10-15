#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 转化为数组的插入排序问题
        # time o(n2)
        # space o(n)
        def list2arr(node):
            arr = []
            while node:
                arr.append(node.val)
                node = node.next
            return arr
        def arr2list(arr):
            dummy = ListNode()
            head = dummy
            while len(arr):
                node = ListNode(arr.pop(0))
                head.next = node
                head = head.next
            return dummy.next

        def insert_sort(arr):
            pass
        arr = list2arr(head)
        arr.sort()
        return arr2list(arr)
# @lc code=end

