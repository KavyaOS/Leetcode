class ListNode(object):
    def __init__(self, data_value):
        self.val = data_value
        self.next = None

class Solution(object):
    '''Worst case Complexities: Space: O(1), time: O(N*k) '''
    def rotateRight(self, head, k):
        if k==0 or head is None or head.next is None:
            return head
        last_but_one = curr = head
        while curr.next.next is not None:
            curr = curr.next
            last_but_one = curr
        last_node = curr.next
        last_node.next = head
        head = last_node
        last_but_one.next = None
        k = k % self.get_list_length(head)
        return self.rotateRight(head, k-1)

    def get_list_length(self, list):
        counter = 0
        while list is not None:
            counter = counter + 1
            list = list.next
        return counter

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
node = S.rotateRight(head_node2, 0)
S.print_values(node)