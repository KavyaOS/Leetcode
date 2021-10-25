import numpy as np
class Solution(object):
    def longestPalindromeSubseq(self, s):
        rows = cols = string_length = len(s)
        DP = np.zeros((string_length, string_length))
        for row in range(rows):
            DP[row][row] = 1
        for substring_length in range(2, len(s)+1):
            for row in range(0, string_length - substring_length + 1):
                col = row + substring_length - 1
                if s[row] == s[col]:
                    if string_length==2:
                        DP[row][col] = 2
                    else:
                        DP[row][col] = 2 + DP[row+1][col-1]
                else:
                    DP[row][col] = max(DP[row+1][col], DP[row][col-1])
        return DP[0][-1]

print(Solution().longestPalindromeSubseq("cac"))