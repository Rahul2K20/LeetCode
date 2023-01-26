class Solution(object):
    def mySqrt(self, x):
        # initializing left and right pointers
        left = 0 
        right = x 
        # use binary search to find the square root
        while (left <= right):
            # calculate mid point
            mid = (left+right)//2
            # if mid*mid is equal to x, return mid
            if mid*mid == x:
                return mid
            # if mid*mid is greater than x, move right pointer to mid-1
            elif mid*mid > x:
                right = mid-1
            # if mid*mid is less than x, move left pointer to mid+1
            else: 
                left = mid + 1
        # return left-1 as the final result
        return left-1