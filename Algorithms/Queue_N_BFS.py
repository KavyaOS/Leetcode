import sys
sys.path.append(r"C://coding/Leetcode")

from Stack_N_Queue.queue import queue

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def BFS(self, root):
        result = []
        q = queue(root)
        while len(q.container)!=0:
            node = q.dequeue()
            result.append(node.val)
            if node.left:
                q.insert(node.left)
            if node.right:
                q.insert(node.right)
        return result

tree = Node(3)
child1 = Node(9)
child2 = Node(20)
child3 = Node(15)
child4 = Node(7)

tree.left = child1
tree.right = child2
child2.left = child3
child2.right = child4

S = Solution()
print(S.BFS(tree))