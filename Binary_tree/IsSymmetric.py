class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if root is None or root.left is None or root.right is None:
            return True
        curr_level_left = [root.left]
        curr_level_right = [root.right]
        while curr_level_left or curr_level_right:
            new_level_left = []
            new_level_right = []
            for node in curr_level_left:
                if node.left:
                    new_level_left.append(node.left)
                if node.right:
                    new_level_left.append(node.right)
            if new_level_left:
                curr_level_left = new_level_left
            for node in curr_level_right:
                if node.left:
                    new_level_right.append(node.left)
                if node.right:
                    new_level_right.append(node.right)
            if new_level_right:
                curr_level_right = new_level_right
            if curr_level_left != curr_level_right[::-1]:
                return False
        return True

tree = Node(1)
child1 = Node(2)
child2 = Node(3)
child3 = Node(4)
child4 = Node(2)
child5 = Node(3)
child6 = Node(4)

tree.right = child1
child1.left = child3
child1.right = child2

tree.left = child4
child4.left = child5
child4.right = child6

S = Solution()
print(S.isSymmetric(tree))