#Hi, here's your problem today. This problem was recently asked by Microsoft:

#Given a string, find the length of the longest substring without repeating characters.

#Here is an example solution in Python language. (Any language is OK to use in an interview, though we'd recommend Python as a generalist language utilized by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)

#class Solution:
 # def lengthOfLongestSubstring(self, s):
    # Fill this in.

#print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10

#Can you find a solution in linear time?

class Solution:
    def lengthOfLongestSubstring(self, s):
        strLen = len(s)
        if strLen < 1:
            return 0
        longestUniqueLength = 1
        lenUniqueString:list = []
        for i in range(strLen-1):
            if s[i] == s[i+1]:
                lenUniqueString.append(longestUniqueLength)
                longestUniqueLength = 1
            else:
                longestUniqueLength += 1
        if len(lenUniqueString) < 1:
            return strLen
        else:
            return max(lenUniqueString)

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
