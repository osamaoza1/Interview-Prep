class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 1:
            return 1
        
        answer = 0 
        for x in range(0, len(s)):
            
            index = x + 1 
            
            while index < len(s) and s[index] not in s[x:index]:
                index += 1 
                
            if len(s[x:index]) > answer:
                answer = len(s[x:index])
                
        return answer 

s = Solution()
print(s.lengthOfLongestSubstring("abcdabc"))
print(s.lengthOfLongestSubstring("ab"))
print(s.lengthOfLongestSubstring("ab"))
print(s.lengthOfLongestSubstring("bbbbbb"))
