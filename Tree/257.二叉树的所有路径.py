#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        path = []
        def dfs(root):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                tmp = str(path[0])
                for s in path[1:]:
                    tmp = tmp + "->" + str(s)
                ans.append(tmp)
            dfs(root.left)
            dfs(root.right)
            path.pop()
        dfs(root)
        return ans

        
# @lc code=end

