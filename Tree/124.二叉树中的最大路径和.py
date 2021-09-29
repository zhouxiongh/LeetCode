#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -sys.maxsize
        def treeSum(root):
            if not root:
                return -sys.maxsize
            l = max(0, treeSum(root.left))
            r = max(0, treeSum(root.right))
            self.ans = max(self.ans, root.val + l + r)
            return root.val + max(l, r)
        treeSum(root)
        return self.ans
# @lc code=end

