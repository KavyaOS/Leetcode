class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    '''Worst case complexities: Space: O(N), Time: O(lgN)'''
    def inorderTraversal(self, root):
        result = []
        return self.inorder_traversal(root, result)
        
    def inorder_traversal(self, root, result):
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.val)
            self.inorder_traversal(root.right, result)
        return result

tree = Node(10)
child1 = Node(20)
child2 = Node(30)

tree.right = child1
child1.left = child2

S = Solution()
print(S.inorderTraversal(tree))