class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    	if p is None and q is None:
    		return True
    	if p is None or q is None:
    		return False
    	if p.val != q.val:
    		return False
    	return self.isSameTree(p.left, q.left) && self.isSameTree(p.right, q.right)