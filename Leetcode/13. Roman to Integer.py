class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mydict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
                  }
        
        result = 0 
        x = 0
        while x < len(s):
            if x+1 < len(s):
                next = mydict[s[x+1]]
                cur = mydict[s[x]]
                if next > cur:
                    result = result + next - cur
                    x += 1
                else:
                    result += cur                
                
            else:
                result += mydict[s[x]]
                
            x += 1
                
        return result 


s1 = Solution()
print(s1.romanToInt("III"))
print(s1.romanToInt("IV"))
print(s1.romanToInt("IX"))
print(s1.romanToInt("LVIII"))
print(s1.romanToInt("MCMXCIV"))