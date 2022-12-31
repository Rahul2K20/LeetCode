class Solution(object):
    def romanToInt(self, s):
        #smaller to larger : subtraction Ex: iv, i is 1 and v is 5 
        #larger to smaller : addition Ex: vi, v is 5 and i is 1 

        hmap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        flag = 0
        
        for i in range(len(s)):
            #subtraction case
            if (i+1 < len(s) and hmap[s[i]] < hmap[s[i+1]]): #i+1<len(s) to prevent out of bounds 
                flag-=hmap[s[i]]

            #addition case
            else:
                flag+=hmap[s[i]]
        
        return flag 
