class ListNode(object):
    def __init__(self, val=None, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        '''Worst case complexities: time: O(N), space: O(1)'''
        if head is None:
            return head
        curr = head
        while curr is not None:
            new = ListNode(curr.val)
            new.next  =curr.next
            curr.next = new
            curr = curr.next.next
        curr = head
        dummy = curr.next
        while curr is not None:
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next
        original_head = head
        curr = head.next
        while curr.next is not None:
            original_head.next = curr.next
            original_head = original_head.next
            curr.next = curr.next.next
            curr = curr.next
        return dummy

    ''' This method is just for testing '''
    def print_values(self, node):
        while node is not None:
            print(node.val)
            node = node.next

head_node1 = ListNode(7)
element_node1 = ListNode(3)
element_node2 = ListNode(11)
element_node3 = ListNode(10)
element_node4 = ListNode(1)

head_node1.next = element_node1
element_node1.next = element_node2
element_node2.next = element_node3
element_node3.next = element_node4

element_node1.random = head_node1
element_node2.random = element_node4
element_node3.random = element_node2
element_node4.random = head_node1

head_node2 = ListNode(3)
element_node5 = ListNode(3)
element_node6 = ListNode(3)

head_node2.next = element_node5
element_node5.next = element_node6

element_node5.random = head_node2


S = Solution()
node = S.copyRandomList(head_node1)
S.print_values(node)