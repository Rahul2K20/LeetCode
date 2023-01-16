class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        common_prefix = strs[0] # Initialize the common_prefix as the first element of the array
        for i in range(1, len(strs)):
            while strs[i].find(common_prefix) != 0: # check if the common_prefix is not a prefix of the current element
                common_prefix = common_prefix[:-1] # shorten the common_prefix by one character
        return common_prefix # return the common_prefix
    
    
# if input = ["flower", "flow", "flight"]:

# The first element of the array is assigned to the variable common_prefix: common_prefix = "flower"
# The loop starts at the second element "flow"
# The condition while strs[i].find(common_prefix) != 0: checks if the common_prefix is a prefix of the current element "flow" using the find() method. Since "flow" starts with "flower" the find() method returns -1, which is not equal to 0, so the loop starts.
# The common_prefix is shortened by one character using the slice notation [:-1]: common_prefix = common_prefix[:-1] which makes common_prefix = "flowe"
# The condition while strs[i].find(common_prefix) != 0: checks again if the common_prefix is a prefix of the current element "flow" using the find() method. Since "flow" starts with "flowe" the find() method returns -1, which is not equal to 0, so the loop continues.
# The common_prefix is shortened by one character again: common_prefix = common_prefix[:-1] which makes common_prefix = "flow"
# The condition while strs[i].find(common_prefix) != 0: checks again if the common_prefix is a prefix of the current element "flow" using the find() method. Since "flow" starts with "flow" the find() method returns 0, which is equal to 0, so the loop stops
# The next element is "flight" and the same process starts again and the loop stops with the common_prefix "fl"
# The function returns "fl" as the longest common prefix of the input array.
