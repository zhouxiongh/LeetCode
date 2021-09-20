#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def DFS(node, depth, ans):
            if node is None:
                return
            while len(ans) <= depth:
                ans.append([])
            ans[depth].append(node.val)
            DFS(node.left, depth+1, ans)
            DFS(node.right, depth+1, ans)
        ans = []
        DFS(root, 0, ans)
        return ans
# @lc code=end

