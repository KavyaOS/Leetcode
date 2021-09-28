# https://leetcode.com/problems/fibonacci-number/submissions/
class Solution(object):
    def fib(self, n):
        # Bottom up approach
        if n == 0:
            return 0
        Fib = []
        for i in range(n+1):
            Fib.append(0)
        Fib[0] = 0
        Fib[1] = 1
        for i in range(2, n+1):
            Fib[i] = Fib[i-1] + Fib[i-2]
        return Fib[n]

print(Solution().fib(6))