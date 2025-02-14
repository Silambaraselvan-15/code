"""

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 """
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1=str1.upper()
        str2=str2.upper()
        
        def div(string,gcd_str):
            if len(string)%len(gcd_str)!=0:
                return False
            return string ==gcd_str*(len(string)//len(gcd_str))

        gcd=math.gcd(len(str1),len(str2))
        gcd_str=str1[:gcd]
        if div(str1,gcd_str) and div(str2,gcd_str):
            return gcd_str
        else:
            return ""
        
    
sol=Solution()
print(sol.gcdOfStrings('ABABAB','ABAB'))
# print(sol.gcdOfStrings('LEET','CODE'))
print(sol.gcdOfStrings('ABCDEF','ABC'))