class Solution(object):
    def firstUniqChar(self, s):

        hmap = {}
        for w in range(len(s)): 
            if s[w] not in hmap: 
                hmap[s[w]] = 1
            else: 
                hmap[s[w]] += 1 
        
        for i in range (len(s)):
            if hmap[s[i]]==1:
                return i

        return -1
            