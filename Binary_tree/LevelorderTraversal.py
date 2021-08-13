class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    '''Worst case complexities: Space: O(N), where N being the number of nodes in the given tree.
     Time: O(M*N), where M being number of levels of a tree, N being maximum number of nodes in a certain level'''
    def levelOrder(self, root):
        if root is None:
            return root
        result = []
        result.append([root.val])
        curr_layer = []
        curr_layer.append(root)
        while curr_layer:
            new_layer = []
            new_level = []
            for node in curr_layer:
                if node.left:
                    new_layer.append(node.left)
                    new_level.append(node.left.val)
                if node.right:
                    new_layer.append(node.right)
                    new_level.append(node.right.val)
            if new_level:
                result.append(new_level)
            curr_layer = new_layer
        return result

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
print(S.levelOrder(tree))