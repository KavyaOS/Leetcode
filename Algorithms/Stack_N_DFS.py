import sys
sys.path.append(r"C://coding/Leetcode")

from Stack_N_Queue.stack import stack

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def DFS(self, root):
        result = []
        s = stack()
        s.push(root)
        while len(s.container)!=0:
            node = s.pop()
            result.append(node.val)
            if node.left:
                s.push(node.left)
            if node.right:
                s.push(node.right)
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
print(S.DFS(tree))