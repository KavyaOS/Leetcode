# https://leetcode.com/problems/edit-distance/
import numpy as np

class Solution(object):
    def minDistance(self, word1, word2):
        ED = np.zeros((len(word1)+1, len(word2)+1))
        diff_matrix = np.zeros((len(word1)+1, len(word2)+1))
        result = 0
        
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0:
                    diff_matrix[i][j] = j
                elif j==0:
                    diff_matrix[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    diff_matrix[i][j] = 0
                else:
                    diff_matrix[i][j] = 1

        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0:
                    ED[i][j] = j
                elif j==0:
                    ED[i][j] = i
                else:
                    ED[i][j] = min(1+ED[i-1][j], 1+ED[i][j-1], diff_matrix[i][j]+ED[i-1][j-1])
                result = int(ED[i][j])

        return result

print(Solution().minDistance("plasma", "altruism"))