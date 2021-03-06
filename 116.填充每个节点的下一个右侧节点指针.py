#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def next_level_nodes(cur_level_nodes):
            nodes = []
            for node in cur_level_nodes:
                nodes.append(node.left)
                nodes.append(node.right)
            return nodes

        
        nodes = [root]
        while nodes[0] and nodes[0].left:
            nodes = next_level_nodes(nodes)
            for i in range(1, len(nodes)):
                nodes[i-1].next = nodes[i]
        return root
            
# @lc code=end

