#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = ""
        def write(node):
            nonlocal ans
            if not node:
                ans = ans + "#,"
            else:
                ans = ans + str(node.val)
                ans = ans + ","
                write(node.left)
                write(node.right)
        write(root)
        return ans

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        def read():
            nonlocal data
            if data[0] == "#":
                data = data[1:]
                return None
            root = TreeNode(data[0])
            data = data[1:]
            root.left = read()
            root.right = read()
            return root
            
        return read()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

