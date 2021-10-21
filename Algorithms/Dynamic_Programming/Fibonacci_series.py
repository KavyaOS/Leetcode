# https://leetcode.com/problems/fibonacci-number/submissions/
class Solution(object):
    def fib(self, n):
        '''Space: O(n), Time: O(n)'''
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

    def fib_topDown(self, n):
        self.compute_fibonacci(n, [])

    def compute_fibonacci(n, Fib):
        if n == 0:
            return 0
        elif n==1: return 1
        else:


print(Solution().fib(6))