"""
There are n kids with candies. You are given an integer array candies, 

where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, 

denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, 

they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.            """

class Solution:
    def kidsWithCandies(self, candy: list[int], extraCandies: int) -> list[bool]:
        result=[]
        candies=candy.copy()
        print(max(candies))
        for i in range(len(candy)):
            candies[i]=candy[i]+extraCandies
            for j in range(len(candy)):
                if candies[i]>=candy[j] and candies[i]>=max(candy) :
                    result.append(True)
                    break
                else:
                    result.append(False)
                    break   
        
        return result

sol=Solution()
print(sol.kidsWithCandies([2,3,8,7,8],1))