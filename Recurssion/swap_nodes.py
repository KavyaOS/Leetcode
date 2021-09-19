class ListNode(object):
    def __init__(self, data_value):
        self.val = data_value
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        if head is None:
            return head
        node = head
        prev = None
        if node.next:
            head = node.next
        while node is not None and node.next is not None:
            if prev: prev.next = node.next
            temp = node.next.next
            node.next.next = node
            prev = node
            node.next = temp
            node = node.next
        return head
    
    ''' This method is just for testing '''
    def print_values(self, node):
        while node is not None:
            print(node.val)
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
new_head = S.swapPairs(head_node1)
S.print_values(new_head)