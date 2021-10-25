'''Naive Approach'''
class Solution(object):
    def is_palindrome(self, s, start, stop):
        if start==stop: return True
        substring = s[start:stop+1]
        reversed_string = substring[::-1]
        if substring==reversed_string:
            return True
        return False
            
    def longestPalindrome(self, s):
        left = right = 0
        result = ""
        if len(s)==1: return s
        for left in range(len(s)):
            for right in range(left, len(s)+1):
                if self.is_palindrome(s, left, right):
                    if right-left >= len(result):
                        result = s[left:right+1]
        return result