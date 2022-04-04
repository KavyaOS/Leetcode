import numpy as np

class Solution(object):
    def minCostClimbingStairs(self, cost):
        DP = np.zeros(len(cost)+1)
        DP[0] = DP[1] = 0
        for i in range(2, len(cost)+1):
            DP[i] = min(DP[i-1] + cost[i-1], DP[i-2] + cost[i-2])
        return DP[len(cost)]

print(Solution().minCostClimbingStairs([10, 15, 25]))