#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # find node
        else:
            new_root = None
            # null left
            if not root.left:
                new_root = root.right
                del root
                return new_root
            # null right
            elif not root.right:
                new_root = root.left
                del root
                return new_root
            # both exist
            else:
                min_right = root.right
                # find succeed node
                while min_right.left:
                    min_right = min_right.left
                root.val = min_right.val
                root.right = self.deleteNode(root.right, min_right.val)
        return root
            
# @lc code=end

