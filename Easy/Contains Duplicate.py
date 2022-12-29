class Solution(object):
    def containsDuplicate(self, nums):
      hmap = {}
      for i in nums: 
        if i in hmap: 
          hmap[i]+=1 
        else: 
          hmap[i]=1 

      for k,v in hmap.items():
        if v >= 2:
          return True 
      return False 