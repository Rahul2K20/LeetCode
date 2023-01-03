class Solution(object):
    def singleNumber(self, nums):
     hmap = {}
     for i in nums:
       if i not in hmap: 
         hmap[i] = 1 
       else: 
         hmap[i] += 1 
      
     for k,v in hmap.items():
       if v==1:
         return k 
         