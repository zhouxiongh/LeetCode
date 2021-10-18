#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.ans = []
        self.count = 0
        self.max_count = 0
        self.val = 0
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            visit(node.val)
            inorder(node.right)
        def visit(val):
            if self.count > 0 and val == self.val:
                self.count += 1
            else:
                self.val = val
                self.count = 1
            if self.count > self.max_count:
                self.max_count = self.count
                self.ans.clear()
            
            if self.count == self.max_count:
                self.ans.append(val)

        inorder(root)
        return self.ans
# @lc code=end

