'''https://leetcode.com/problems/longest-common-subsequence/submissions/'''
import numpy as np
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        DP = np.zeros((len(text1), len(text2)))
        for i in range(len(text1)):
            for j in range(len(text2)):
                if i==0: DP[i][j] = 0
                if j==0: DP[i][j] = 0
                    
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i]==text2[j]:
                    DP[i][j] = 1+DP[i-1][j-1]
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        return int(DP[len(text1)-1][len(text2)-1])

print(Solution().longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy"))