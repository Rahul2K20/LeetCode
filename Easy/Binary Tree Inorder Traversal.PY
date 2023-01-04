#Inorder traversal: Left, root, right 
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
#Building the list recursivly. 
#Simply add the returned list from the left and right trees together with the value in the current node.
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
