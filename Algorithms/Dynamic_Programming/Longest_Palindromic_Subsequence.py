import numpy as np
class Solution(object):
    def longestPalindromeSubseq(self, s):
        rows = cols = string_length = len(s)
        DP = np.zeros((string_length, string_length))
        for row in range(rows):
            DP[row][row] = 1
        for k in range(1, len(s)):
            for row in range(rows-k):
                col = row + k
                if s[row] == s[col]:
                    DP[row][col] = 2 + DP[row+1][col-1]
                else:
                    DP[row][col] = max(DP[row+1][col], DP[row][col-1])

        return int(DP[0][-1])

print(Solution().longestPalindromeSubseq("bbbab"))