class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
    	List<Integer> re = new ArrayList<Integer>();
    	preorderTraversal1(root, re);
    	return re;

    }

    private void preorderTraversal1(TreeNode node, List<Integer> re) {
    	if (node == null) {
    		return;
    	}
    	re.add(node.val);
    	preorderTraversal1(node.left, re);
    	preorderTraversal1(node.right, re);
    }
}