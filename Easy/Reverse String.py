class Solution(object):
    def reverseString(self, s):

     #two pointer approach
     left = 0 
     right = len(s)-1

     while(left<right):
         s[left], s[right] = s[right], s[left]
         left+=1
         right-=1

     print(s)
      
      
    #   #pythonic approach
    #   s[:] = s[::-1]
    #   s = s.reverse()
