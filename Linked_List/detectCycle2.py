class ListNode(object):
    def __init__(self, data_value):
        self.data_value = data_value
        self.next_node = None

class Solution(object):
    def detectCycle(self, head):
        if head is None:
            return None
        counter = self.get_indexOfNode(head)
        i = 0
        if counter is None:
            return None
        while i!=counter-1:
            head = head.next_node
            i = i + 1
        return head

    def get_indexOfNode(self, head):
        slow = head
        fast = head.next_node
        counter = 0
        while slow!=fast:
            if fast is None or fast.next_node is None:
                return None
            slow = slow.next_node
            fast = fast.next_node.next_node
            counter = counter + 1
        return counter
            

head_node = ListNode(3)
element_node1 = ListNode(2)
element_node2 = ListNode(0)
element_node3 = ListNode(-4)

head_node.next_node = element_node1
element_node1.next_node = element_node2
element_node2.next_node = element_node3
#element_node3.next_node = element_node1

S = Solution()
print(S.hasCycle(head_node))