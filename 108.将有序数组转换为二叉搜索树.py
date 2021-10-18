#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildBST(l, r):
            if l > r:
                return None
            m = l + (r - l) // 2
            root = TreeNode(nums[m])
            root.left = buildBST(l, m-1)
            root.right = buildBST(m+1, r)
            return root
        return buildBST(0, len(nums)-1)
# @lc code=end

