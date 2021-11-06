from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        degree = [0] * numCourses
        adj_list = [[] for x in range(numCourses)]
        queue = []
        
        for course1, course2 in prerequisites:
            degree[course1] = degree[course1] + 1
            adj_list[course2].append(course1)
            
        for k in range(numCourses):
            if degree[k] == 0:
                queue.append(k)
                
        counter = 0
        topological_sorted_order = []
        
        while queue:
            key = queue.pop()
            topological_sorted_order.append(key)
            counter = counter + 1
            for node in adj_list[key]:
                degree[node] = degree[node] - 1
                if degree[node] == 0:
                    queue.append(node)
                    
        if counter!= numCourses:
            return []
        
        return topological_sorted_order

print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))