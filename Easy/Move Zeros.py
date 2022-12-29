class Solution(object):
    def moveZeroes(self, nums):
       j = 0 
       for i in range(len(nums)): 
           if nums[i] != 0: 
               nums[i],nums[j] = nums[j], nums[i]
               j+=1
       return nums
               
               
# We use i to keep track of position of the first zero in the list (which changes as we go).
# We use j to keep track of the first non-zero value after the first zero (which is pointed by i).
# Each time we have i correctly points to a zero and j correctly points to the first non-zero after i, we swap the values that store at i and j.
# By doing this, we move zeros towards the end of the list gradually until j reaches the end.
# And when it does, we are done.