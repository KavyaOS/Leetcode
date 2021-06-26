class ListNode(object):
    def __init__(self, data_value):
        self.data_value = data_value
        self.next = None

class Solution(object):
    ''' Time complexity: O(N) - N being the size of the list, Space: O(1) - constant space'''
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        ref_node = head
        next_to_ref = ref_node.next
        while next_to_ref is not None:
            temp = next_to_ref.next
            next_to_ref.next = head
            ref_node.next = temp
            head = next_to_ref
            next_to_ref = ref_node.next
        return head

    ''' This method is just for testing '''
    def print_values(self, node):
        while node is not None:
            print(node.data_value)
            node = node.next

head_node1 = ListNode(1)
element_node1 = ListNode(2)
element_node2 = ListNode(3)
element_node3 = ListNode(4)
element_node4 = ListNode(5)

head_node1.next = element_node1
element_node1.next = element_node2
element_node2.next = element_node3
element_node3.next = element_node4

S = Solution()
node = S.reverseList(head_node1)
S.print_values(node)