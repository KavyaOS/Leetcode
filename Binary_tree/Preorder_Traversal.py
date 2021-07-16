class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    '''Worst case complexities: Space: O(N), Time: O(lgN)'''
    def preOrderTraversal(self, root):
        result = []
        if root:
            result.append(root.val)
            result = result + self.preOrderTraversal(root.left)
            result = result + self.preOrderTraversal(root.right)
        return result

tree = Node(10)
child1 = Node(20)
child2 = Node(30)

tree.right = child1
child1.left = child2

S = Solution()
print(S.preOrderTraversal(tree))