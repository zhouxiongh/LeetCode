# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
    	re = []
    	self.postorderTraversal1(root, re)
    	return re

    def postorderTraversal1(self, node, re):
    	if node is None:
    		return

    	self.postorderTraversal1(node.left, re)
    	self.postorderTraversal1(node.right, re)
    	re.append(node.val)