class Solution(object):
    def majorityElement(self, nums):
     #hashmap approach

     n = len(nums)
     target = n/2
     hmap = {}

     for i in nums: 
        if i in hmap: 
            hmap[i]+=1 
        else: 
            hmap[i]=1 

     for k,v in hmap.items():
         if v > target: 
             return k 
