class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    '''Worst case complexities: 
        Space (To hold result): O(l*n), where l being the number of levels of a binary tree and n being the number of nodes at a certain level
        Time: O(2^l) or O(n), since in worst case n can go upto 2^l'''
    def levelOrder(self, root):
        if root is None:
            return root
        result = []
        def helper_traversal(level, node):
            '''Helper function which returns nothing but arranges result in proper format'''
            if node:
                if len(result)<=level:
                    result.append([node.val])
                else:
                    result[level].append(node.val)
                helper_traversal(level+1, node.left)
                helper_traversal(level+1, node.right)
        helper_traversal(0, root)
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
print(S.levelOrder(tree))