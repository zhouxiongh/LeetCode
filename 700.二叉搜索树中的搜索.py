#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def searchBST1(node, val):
            if not node:
                return None
            if val == node.val:
                return node
            if val < node.val:
                return searchBST1(node.left, val)
            else:
                return searchBST1(node.right, val)
        return searchBST1(root, val)
# @lc code=end

