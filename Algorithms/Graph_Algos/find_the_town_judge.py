'''Time: O(n), space:O(1)'''
class Solution:
    def findJudge(self, n,trust):
        does_trust = {i+1:False for i in range(n)}
        being_trusted = {i+1:[] for i in range(n)}
        
        for p1, p2 in trust:
            does_trust[p1] = True
            being_trusted[p2].append(p1)
            
        for i in range(1, n+1):
            if does_trust[i] == False and len(being_trusted[i])==n-1:
                return i
        return -1
            
print(Solution().findJudge(3, [[1,2], [1,3]]))