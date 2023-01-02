class Solution(object):
    def hammingWeight(self, n):
        count = 0 
        while(n!=0):
            #if the and operation yeilds 1, increment count 
            if n&1==1: 
                count+=1 
            #shift bits to the right by 1
            n = n>>1
        return count 

