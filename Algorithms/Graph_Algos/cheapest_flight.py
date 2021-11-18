class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        dist_from_src = [float('inf')] * n
        dist_from_src[src] = 0
        for i in range(k+1):
            temp_dist = dist_from_src.copy()
            for u, v, cost_u_v in flights:
                if dist_from_src[u] + cost_u_v < temp_dist[v]:
                    temp_dist[v] = dist_from_src[u] + cost_u_v
            dist_from_src = temp_dist

        return -1 if dist_from_src[dst] == float('inf') else dist_from_src[dst]

print(Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))
#print(Solution().findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1))
#print(Solution().findCheapestPrice(5, [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]], 0, 4, 1))
#print(Solution().findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], 0, 2, 2))