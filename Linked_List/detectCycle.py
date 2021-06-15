# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, data_value):
        self.data_value = data_value
        self.next_node = None

class Solution(object):
    def hasCycle(self, head):
        nodes_seen = []
        while head is not None:
            if head in nodes_seen:
                return True
            else:
                nodes_seen.append(head)
                head = head.next_node
        
        return False

head_node = ListNode(3)
element_node1 = ListNode(2)
element_node2 = ListNode(0)
element_node3 = ListNode(-4)

head_node.next_node = element_node1
element_node1.next_node = element_node2
element_node2.next_node = element_node3
# element_node3.next_node = element_node1

S = Solution()
print(S.hasCycle(head_node))