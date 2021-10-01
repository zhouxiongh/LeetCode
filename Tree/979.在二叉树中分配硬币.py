#
# @lc app=leetcode.cn id=979 lang=python3
#
# [979] 在二叉树中分配硬币
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # balance = node.val - 1 + balance(node.left) + balance(node.right)
    # flow = abs(balance)
    # ans = flow(root.left) + flow(root.right)
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        def balance(root):
            if not root:
                return 0
            l = balance(root.left)
            r = balance(root.right)
            self.ans = abs(l) + abs(r) + self.ans
            return root.val - 1 + l + r
        balance(root)
        return self.ans
# @lc code=end

