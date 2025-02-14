"""

You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

"""

class Solution:
    def mergeAlternately(self,word1:str,word2:str) -> str:
        merge=''
        diff=min(len(word1),len(word2))
        if len(word1)==len(word2):
            for i in range(len(word1)):
                merge+=word1[i]+word2[i]
        elif len(word1)>len(word2):
            for i in range(len(word2)):
                merge+=word1[i]+word2[i]
            merge+=word1[diff:]
        else:
            for i in range(len(word1)):
                merge+=word1[i]+word2[i]
            merge+=word2[diff:]
       

        return merge
sol=Solution()
new=sol.mergeAlternately('cdf','qa')
print(new)