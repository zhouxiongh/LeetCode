#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        def rob(root):
            if not root:
                return 0, 0, 0
            l, ll, lr = rob(root.left)
            r, rl, rr = rob(root.right)
            return max(root.val + ll + lr + rl + rr, l + r), l, r
        return rob(root)[0]
# @lc code=end

