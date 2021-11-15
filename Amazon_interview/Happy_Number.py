'''https://leetcode.com/problems/happy-number/'''
class Solution(object):
    def get_next_num(self, num):
        result = 0
        while num!=0:
            result = result + (num%10)**2
            num = num//10
        return result
        
    def isHappy(self, n):
        seen_nums = []
        while n>1:
            if n not in seen_nums:
                seen_nums.append(n)
            else:
                return False
            n = self.get_next_num(n)
        return n==1

print(Solution().isHappy(161))