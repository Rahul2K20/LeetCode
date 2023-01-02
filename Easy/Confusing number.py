class Solution(object):
    def confusingNumber(self, n):
        #convert n to a string so its an iterable 
        S = str(n)
        #keep a list to store the mapping result 
        result = []
        #map the inverted numbers 
        rotation = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}

        #iterate through S 
        for i in S:
            #if theres no mapping of the number, return false 
            if i not in rotation: 
                return False 
            #if a mapping exists, store the mapped version in the list 
            else:  
                result.append(rotation[i])
        
        #remove the string quotes 
        result = "".join(result)

        #compare the reversed list to the original number 
        #ex 89 rotated becomes 68, but 68!=89 and hence it is a confusing number 
        return int(result[::-1])!=n