#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidBST1(root, min_val, max_val):
            if not root:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            return isValidBST1(root.left, min_val, root.val) and isValidBST1(root.right, root.val, max_val)
        return isValidBST1(root, -sys.maxsize, sys.maxsize)

# @lc code=end

