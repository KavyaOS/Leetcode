class Solution(object):
    def longestPalindromeSubseq(self, s):
        if len(s)==1: return 1
        T = [[0]*(len(s)+1)]*(len(s)+1)
        for i in range((len(s))):
            T[i][i] = 1
            for j in range((len(s))):
                if i>j:
                    T[i][j] = 0

        for i in range(1,len(s)):
            for j in reversed(range((len(s)-i+1))):
                if s[i] == s[j]:
                    T[i][j] = max(2 + T[i+1][j-1] , T[i+1][j], T[i][j-1])
                else:
                    T[i][j] = max(T[i+1][j], T[i][j-1])
        return T[1][len(s)]

        """
        :type s: str
        :rtype: int
        """

print(Solution().longestPalindromeSubseq("cac"))