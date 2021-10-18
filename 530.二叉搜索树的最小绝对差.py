#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            # something
            if self.prev is not None:
                self.min_diff = min(self.min_diff, abs(self.prev.val - node.val))
            self.prev = node
            inorder(node.right)
        self.prev = None
        self.min_diff = sys.maxsize
        inorder(root)
        return self.min_diff
# @lc code=end

