class ListNode(object):
    def __init__(self, data_value):
        self.val = data_value
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return head
        prev=head
        cur = head.next
        while cur is not None:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head

    ''' This method is just for testing '''
    def print_values(self, node):
        while node is not None:
            print(node.val)
            node = node.next

head_node1 = ListNode(1)
element_node1 = ListNode(2)
element_node2 = ListNode(6)
element_node3 = ListNode(3)
element_node4 = ListNode(4)
element_node5 = ListNode(5)
element_node6 = ListNode(6)

head_node1.next = element_node1
element_node1.next = element_node2
element_node2.next = element_node3
element_node3.next = element_node4
element_node4.next = element_node5
element_node5.next = element_node6

head_node2 = ListNode(1)
element_node7 = ListNode(2)
element_node8 = ListNode(2)
element_node9 = ListNode(1)

head_node2.next = element_node7
element_node7.next = element_node8
element_node8.next = element_node9

S = Solution()
node = S.removeElements(head_node1, 6)
S.print_values(node)