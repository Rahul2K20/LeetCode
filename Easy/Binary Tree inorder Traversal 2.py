#Inorder traversal: Left, root, right 
#Iterative approach 
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        stack = []
        cur = root 
        while cur or stack: 
            while cur:
                stack.append(cur)
                cur = cur.left 
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right 
        return res