class ListNode(object):
    def __init__(self, data_value):
        self.data_value = data_value
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ''' Time Complexity: O(M+N), Space: O(M) 
        nodes_seen = set()
        while headA is not None:
            nodes_seen.add(headA)
            headA = headA.next
        while headB is not None:
            if headB in nodes_seen:
                return headB
            headB = headB.next
        return None'''

        ''' Time Complexity: O(M+N), Space: O(1) '''
        pA = headA
        pB = headB
        while pA!=pB:
            if pA is None:
                pA = headB
            else:
                pA = pA.next
            if pB is None:
                pB = headA
            else:
                pB = pB.next
        return pA

    def get_list_length(self, list):
        counter = 0
        while list is not None:
            counter = counter + 1
            list = list.next
        return counter

    def print_values(self, node):
        while node is not None:
            print(node.data_value)
            node = node.next

head_node1 = ListNode(4)
element_node1 = ListNode(1)
element_node2 = ListNode(8)
element_node3 = ListNode(4)
element_node4 = ListNode(5)

head_node1.next = element_node1
element_node1.next = element_node2
element_node2.next = element_node3
element_node3.next = element_node4

head_node2 = ListNode(5)
element_node5 = ListNode(6)
element_node6 = ListNode(1)

head_node2.next = element_node5
element_node5.next = element_node6
element_node6.next = element_node2

S = Solution()
'''S.print_values(head_node1)
print("1 done")
S.print_values(head_node2)'''
print(Solution().getIntersectionNode(head_node1, head_node2))