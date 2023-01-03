#Recursive solution
class Solution(object):
    def maxDepth(self, root):
     #base case 
     if not root: 
         return 0 
     #recursive case 
     else: 
         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))