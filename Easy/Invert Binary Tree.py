class Solution(object):
    def invertTree(self, root):
        #Base case 
        if not root: 
            return None
        #Recursive case
        else: 
            root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root
        