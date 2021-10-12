#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # def reverse(l1):
            # pass
        # def addTwoNumbers1(l1, l2):
            # pass
        # return reverse(addTwoNumbers1(reverse(l1), reverse(l2)))

        # 进阶：如果输入链表不能修改该如何处理？
        # 换句话说，不能对列表中的节点进行翻转
        # use stack
        import collections
        s1 = collections.deque()
        s2 = collections.deque()
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        head = None
        sum = 0
        while len(s1) or len(s2) or sum:
            sum += s1.pop() if len(s1) else 0
            sum += s2.pop() if len(s2) else 0
            n = ListNode(sum % 10)
            sum //= 10
            n.next = head
            head = n
        return head


# @lc code=end

