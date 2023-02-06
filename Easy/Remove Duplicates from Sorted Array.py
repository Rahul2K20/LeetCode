class Solution(object):
    def removeDuplicates(self, nums):
     
     # nums[0:] = sorted(set(nums))
     # return len(nums)

    #  j=1
    #  if len(nums) == 0:
    #     return 0
    
    #  for i in range(1,len(nums)): 
    #    if nums[i] != nums[i-1]:
    #      nums[j] = nums[i]
    #      j+= 1 
        
    #  return j

      j = 1 

      for i in range (1,len(nums)):
        if nums[i] != nums[i-1]: 
          nums[j] = nums[i]
          j+=1 
      
      return nums 
        
     
        
         
            