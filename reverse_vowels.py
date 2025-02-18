"""Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', 

and they can appear in both lower and upper cases, more than once."""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        string=list(s)
        vow_found=[]
        for i in range(len(string)):
            if string[i] in vowels:
                vow_found.append(string[i])
        vow_found.reverse()
        k=0
        for i in range(len(string)):
            if string[i] in vowels:
                string[i]=vow_found[k]
                k+=1
        return ''.join(string)
    
sol=Solution()
print(sol.reverseVowels("IceCreAm"))