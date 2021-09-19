class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
    	List<Integer> re = new ArrayList<Integer>();
    	postorderTraversal1(root, re);
    	return re;
    }

    private void postorderTraversal1(TreeNode node,List<Integer> re) {
    	if (node == null) {
    		return;
    	}
    	postorderTraversal1(node.left, re);
    	postorderTraversal1(node.right, re);
    	re.add(node.val);
    }
}