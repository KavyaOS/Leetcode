'''https://leetcode.com/problems/longest-palindromic-substring/'''
import numpy as np
class Solution(object):        
    def longestPalindrome(self, s):
        DP = np.zeros((len(s), len(s)))
        max_len = 1
        result = ""
        start = end = 0
        string_length = rows = cols = len(s)
        for row in range(rows):
            DP[row][row] = 1
            col = row + 1
            if col<cols:
                if s[row]==s[col]:
                    DP[row][col] = 1
                    start = row
                    end = col
                else: DP[row][col] = 0

        for k in range(2, len(s)):
            for row in range(rows-k):
                col = row + k
                #print(row, col)
                if s[row] == s[col] and int(DP[row+1][col-1])==1:
                        DP[row][col] = 1
                        if col-row >= max_len:
                            start = row
                            end = col

                else:
                    DP[row][col] = 0
                
        return s[start:end+1]

print(Solution().longestPalindrome("aaaabbaa"))
#print(Solution().longestPalindrome("cbbd"))