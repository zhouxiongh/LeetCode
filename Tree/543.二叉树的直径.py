#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth = 0
        def dfs(root):
            if not root:
                return -1
            l = dfs(root.left) + 1
            r = dfs(root.right) + 1
            self.depth = max(self.depth, l+r)
            return max(l, r)
        dfs(root)
        return self.depth

# @lc code=end

