#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    cached_node = {}
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        if head not in self.cached_node:
            new_head = Node(head.val)
            self.cached_node[head] = new_head
            new_head.next = self.copyRandomList(head.next)
            new_head.random = self.copyRandomList(head.random)
        return self.cached_node[head]
        
# @lc code=end

