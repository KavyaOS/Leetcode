class ListNode(object):
    def __init__(self, data_value):
        self.val = data_value
        self.next = None

class Solution(object):
    '''Worst case Complexities: Space: O(1), time: O(N) '''
    def rotateRight(self, head, k):
        if head is None or k == 0 or head.next is None:
            return head
        curr = head
        counter = 1
        while curr.next is not None:
            counter = counter + 1
            curr = curr.next
        curr.next = head
        k = counter - (k%counter)
        while k!=0:
            curr = curr.next
            k = k-1
        new_head = curr.next
        curr.next = None
        return new_head
        
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

head_node2 = ListNode(0)
element_node = ListNode(1)
element_node4 = ListNode(2)
head_node2.next = element_node
element_node.next = element_node4

S = Solution()
node = S.rotateRight(head_node1, 2)
S.print_values(node)