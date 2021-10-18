#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return -1
            x = inorder(node.left)
            if self.k == 0:
                return x
            self.k -= 1
            if self.k == 0:
                return node.val
            return inorder(node.right)
        self.k = k
        return inorder(root)
# @lc code=end

