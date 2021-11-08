from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        visited = defaultdict(list)
        post = defaultdict(list)
        adj_list = defaultdict(list)
        result = []

        for course1, course2 in prerequisites:
            adj_list[course1].append(course2)
            visited[course1] = False

        def explore(vertex):
            visited[vertex] = True
            for node in adj_list[vertex]:
                if visited[node] == False:
                    explore(node)
            result.append(node)

        explore(prerequisites[0])
        return result

print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))