import math
class Solution(object):
    ## Time: O(sqrt(n) * log(logn)), Space: O(n)
    def countPrimes(self, n):
        numbers = [False, False] + [True]*(n-2)
        for p in range(2, int(math.sqrt(n))+1):
            if numbers[p]:
                for multiples in range(p*p, n, p):
                    numbers[multiples] = False
        # count = 0
        # # for value in numbers:
        # #     if value:
        # #         count+=1
        # # return count
        return sum(numbers)

print(Solution().countPrimes(10))