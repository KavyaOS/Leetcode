'''https://leetcode.com/problems/palindrome-number/'''

class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        num = x
        reversed_num = 0
        while x!=0:
            reversed_num = reversed_num*10 + (x%10)
            x = x / 10
            
        if num==reversed_num:
            return True
        return False

print(Solution().isPalindrome(-424))