class Solution(object):
    def twoSum(self, nums, target):

    #  #brute force o(n^2)
    #   n = len(nums)
    #   for i in range(0,n):
    #      for j in range (i+1, n):
    #          if nums[i] + nums[j] == target: 
    #              return i,j
      
      #hashmap o(n)
      #rationale: target = nums[i] + x; x = target - nums[i]

      hmap = {}
      for i in range (0,len(nums)):
          x = target - nums[i]
          if x in hmap: 
              return [hmap[x],i]
          else: 
              hmap[nums[i]] = i 
      