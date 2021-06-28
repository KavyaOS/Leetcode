class ListNode(object):
    def __init__(self, data_value):
        self.val = data_value
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        ''' Worst case complexities: time: O(N-2), space: O(1)'''
        if head is None or head.next is None or head.next.next is None:
            return head
        odd= odd_head  = head
        even = even_head = head.next
        counter = 3
        head = head.next.next
        while head is not None:
            if counter %2 !=0:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            counter = counter + 1
        odd.next = even_head
        even.next = None
        return odd_head

    ''' This method is just for testing '''
    def print_values(self, node):
        while node is not None:
            print(node.val)
            node = node.next

head_node1 = ListNode(2)
element_node1 = ListNode(1)
element_node2 = ListNode(3)
element_node3 = ListNode(5)
element_node4 = ListNode(6)
element_node5 = ListNode(4)
element_node6 = ListNode(7)

head_node1.next = element_node1
element_node1.next = element_node2
element_node2.next = element_node3
element_node3.next = element_node4
element_node4.next = element_node5
element_node5.next = element_node6

head_node2 = ListNode(1)
element_node7 = ListNode(2)
element_node8 = ListNode(3)
element_node9 = ListNode(4)

head_node2.next = element_node7
element_node7.next = element_node8
element_node8.next = element_node9

S = Solution()
node = S.oddEvenList(head_node2)
S.print_values(node)