class Solution(object):
    def isSymmetric(self, root):
        if not root: 
            return 
        def mirror (l,r): 
            if not l and not r:
                return True
            
            if l and r: 
                #if left and right subtrees are not equals, the tree is not symmetrical 
                if l.val != r.val: 
                    return False 
                     #Do the same process recursively for every other subtree 
                return mirror(l.left, r.right) & mirror(r.left, l.right)
            else:    
                return False 
        
        return mirror(root.left, root.right)