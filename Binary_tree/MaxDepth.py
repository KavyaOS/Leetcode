class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    '''Worst case complexities: Space: O(N), where N being the number of nodes in the given tree.
     Time: O(M*N), where M being number of levels of a tree, N being maximum number of nodes in a certain level'''
    def maxDepth(self, root):
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

tree = Node(3)
child1 = Node(9)
child2 = Node(20)
child3 = Node(15)
child4 = Node(7)

tree.right = child1
child1.left = child2
child2.left = child3
child2.right = child4

S = Solution()
print(S.maxDepth(tree))