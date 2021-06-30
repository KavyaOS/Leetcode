class ListNode(object):
    def __init__(self, data_value):
        self.val = data_value
        self.next = None

class Solution(object):
    '''Worst case Complexities: Space: O(1), time: O(N) where N being the size of the longest list'''
    def mergeTwoLists(self, l1, l2):
        result = head = ListNode(-1)
        while l1 is not None and l2 is not None:
            if l1.val<=l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        while l1 is not None:
            head.next = l1
            l1 = l1.next
            head = head.next
        while l2 is not None:
            head.next = l2
            l2 = l2.next
            head = head.next
        return result.next

    ''' This method is just for testing '''
    def print_values(self, node):
        while node is not None:
            print(node.val)
            node = node.next

head_node1 = ListNode(1)
element_node1 = ListNode(2)
element_node2 = ListNode(3)
element_node3 = ListNode(4)

head_node1.next = element_node1
element_node1.next = element_node2
element_node2.next = element_node3

head_node2 = ListNode(5)
element_node7 = ListNode(6)
element_node8 = ListNode(7)
element_node9 = ListNode(8)

head_node2.next = element_node7
element_node7.next = element_node8
element_node8.next = element_node9

head_node3 = ListNode(None)
head_node4 = ListNode(0)

S = Solution()
node = S.mergeTwoLists(None, head_node4)
S.print_values(node)