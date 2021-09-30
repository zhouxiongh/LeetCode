#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            pl = 0
            pr = 0
            if root.left and root.left.val == root.val:
                pl = l + 1
            if root.right and root.right.val == root.val:
                pr = r + 1
            self.ans = max(self.ans, pl + pr)
            return max(pl, pr)
        dfs(root)
        return self.ans
# @lc code=end

