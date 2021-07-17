class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    '''Worst case complexities: Space: O(N), Time: O(lgN)'''
    def postorderTraversal(self, root):
        result = []
        return self.postorder_traversal(root, result)
        
    def postorder_traversal(self, root, result):
        if root:
            self.postorder_traversal(root.left, result)
            self.postorder_traversal(root.right, result)
            result.append(root.val)
        return result

tree = Node(10)
child1 = Node(20)
child2 = Node(30)

tree.right = child1
child1.left = child2

S = Solution()
print(S.postorderTraversal(tree))