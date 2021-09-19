class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
    		List<Integer> re = new ArrayList<Integer>();
    		inorderTraversal1(root, re);
    		return re;
    }

    private void inorderTraversal1(TreeNode node, List<Integer> re) {
        if (node == null) {
            return;
        }
      	inorderTraversal1(node.left, re);
      	re.add(node.val);
      	inorderTraversal1(node.right, re);
    }
}