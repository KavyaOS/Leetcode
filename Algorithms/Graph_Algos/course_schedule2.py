from collections import defaultdict
class Solution(object):
    pre = {}
    post = {}
    clock = 0
    visited = {}
    order = []
    prerequisites = []

    def has_cycle(self):
        for u,v in self.prerequisites:
            if self.post[u]<self.post[v]:
                return True
        return False

    def neighbour(self, v):
        return [u[1] for u in self.prerequisites if u[0] == v]

    def explore(self, v):
            self.visited[v] = True
            self.pre[v] = self.clock
            self.clock += 1
            for u in self.neighbour(v):
                if not self.visited[u]:
                    self.explore(u)
            self.post[v] = self.clock
            self.order.append(v)
            self.clock += 1

    def findOrder(self, numCourses, prerequisites):
        self.visited = {i:False for i in range(numCourses)}
        self.prerequisites = prerequisites
        self.order = []
        for u in range(numCourses):
            if not self.visited[u]:
                self.explore(u)
        if self.has_cycle():
            return []
        return self.order
    
print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))