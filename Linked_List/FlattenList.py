class ListNode(object):
    def __init__(self, val=None, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        curr = tail = head
        while curr.child is not None:
            tail = tail.next
        while curr is not None:
            if curr.child is not None:
                tail.next = curr.child
                #tail = tail.next
                while tail.next is not None:
                    tail = tail.next
            curr = curr.next
        return head

    ''' This method is just for testing '''
    def print_values(self, node):
        while node is not None:
            print(node.val)
            node = node.next

head_node1 = ListNode(1)
element_node1 = ListNode(2, head_node1, None)
element_node2 = ListNode(3, element_node1, None)
element_node3 = ListNode(4 ,element_node2, None)
element_node4 = ListNode(5, element_node3, None)
element_node5 = ListNode(6, element_node4, None)
element_node6 = ListNode(7, element_node5, None)
element_node7 = ListNode(8, element_node6, None)
element_node8 = ListNode(9, element_node7, None)
element_node9 = ListNode(10, element_node8, None)
element_node10 = ListNode(11, element_node9, None)
element_node11 = ListNode(12, element_node10, None)

head_node1.next = element_node1
element_node1.next = element_node2
element_node2.next = element_node3
element_node3.next = element_node4
element_node4.next = element_node5

element_node6.next = element_node7
element_node7.next = element_node8
element_node8.next = element_node9

element_node10.next = element_node11

element_node2.child = element_node6
element_node7.child = element_node10

S = Solution()
node = S.flatten(head_node1)
S.print_values(node)

# print(element_node1.prev.val)