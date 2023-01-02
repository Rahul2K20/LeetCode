class Solution(object):
    def isAnagram(self, s, t):
    
    #Account for a case when the length of strings arent equal 
     if len(s)!= len(t):
         return False 

    #Create a count_map of s 
     hmap = {}
     for i in s: 
         if i not in hmap: 
             hmap[i] = 1 
         else: 
             hmap[i]+= 1 

     #check if t exists in the hashmap. if it does, subtract the value by 1 
     for i in t: 
         if i in hmap: 
             hmap[i]-=1 

     #if after subtraction, the value goes lower than 0, it means that t doesn't exist in hashmap         
             if hmap[i] < 0: 
              return False 
    
    #if one of the charas in string t doesnt exist in the hashmap, return False 
         else: 
             return False

    #if the loop exists without ever reaching the if statements, it means the strings are anagrams
     return True 
      