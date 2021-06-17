class ListNode(object):
    def __init__(self, data_value):
        self.data_value = data_value
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        fast = slow = head
        while fast is not None and fast.next is not None and slow is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                while fast!=slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None

head_node = ListNode(3)
element_node1 = ListNode(2)
element_node2 = ListNode(0)
element_node3 = ListNode(-4)

head_node.next = element_node1
element_node1.next = element_node2
element_node2.next = element_node3
element_node3.next = element_node1

S = Solution()
print(S.detectCycle(head_node))