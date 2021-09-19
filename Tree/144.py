# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal1(self, node, re):
    	if node is None:
    		return
    	re.append(node.val)
    	self.preorderTraversal1(node.left, re)
    	self.preorderTraversal1(node.right, re)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        re = []
        self.preorderTraversal1(root, re)
        return re
