#Iterative DFS solution
from collections import deque
class Solution(object):
    def maxDepth(self, root):
      stack = [[root, 1]]
      res = 0 
      while stack: 
          node, depth = stack.pop()
          if node: 
              res = max(res,depth)
              stack.append([node.left,1 + depth])
              stack.append([node.right,1 + depth]) 
      return res 

