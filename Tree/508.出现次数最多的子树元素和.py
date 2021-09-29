#
# @lc app=leetcode.cn id=508 lang=python3
#
# [508] 出现次数最多的子树元素和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        def treeSum(root):
            if not root:
                return 0
            s = root.val + treeSum(root.left) + treeSum(root.right)
            f[s] += 1
            return s
        f = collections.Counter()
        treeSum(root)
        max_freq = max(f.values())
        return [s for s in f.keys() if f[s] == max_freq]
            
            

                
        
# @lc code=end

