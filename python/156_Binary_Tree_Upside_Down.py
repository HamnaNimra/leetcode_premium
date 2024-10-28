"""
Intuition
The new root will be the left most node. 
The tricky part to Figure out is that all you need 
to do as you come back from the left most node is to 
update the current node using the rotation mentioned 
in the problem description since the deeper level 
already is pointing to the node which will be 
the new node in this level already.

Approach
You will have to call the function recursively to 
reach the most bottom node. 
From there, you will perform the rotation 
using the mentioned 
logic(left node becoming the parent, 
    right node becoming the left node 
    and the parent node becoming the right node). 
As previously mentioned the left child node here 
which has become the parent in this level is already 
set as the right child of the lower level so 
there is no need to do anything else

Complexity
N is the number of nodes in the tree

Time complexity:
O(N)
Space complexity:
O(N)

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root: return None
        if not root.left and not root.right: return root
        res = self.upsideDownBinaryTree(root.left)
        new_root = root.left
        new_root.left = root.right
        new_root.right = root
        root.left = None # original root should be a leaf now.
        root.right = None
        return res
        