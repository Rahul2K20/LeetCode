class Solution(object):
    def isPowerOfThree(self, n):
      if n <= 0:
            return False
      return 3**round(math.log(n, 3)) == n
            
        