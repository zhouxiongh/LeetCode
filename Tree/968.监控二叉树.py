#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class State:
    NONE = 0
    COVERD = 1
    CAMERA = 2

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return State.COVERD
            l = dfs(root.left)
            r = dfs(root.right)
            if l == State.NONE or r == State.NONE:
                self.ans = self.ans + 1
                return State.CAMERA
            if l == State.CAMERA or r == State.CAMERA:
                return State.COVERD
            return State.NONE
        if dfs(root) == State.NONE:
            self.ans = self.ans + 1
        return self.ans
# @lc code=end

