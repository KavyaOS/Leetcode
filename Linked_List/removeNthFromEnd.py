class ListNode(object):
    def __init__(self, data_value):
        self.data_value = data_value
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        '''Time complexity: O(N), Space: O(1) '''
        list_len = self.get_list_length(head)
        if list_len == 1 and n==1:
            head = None
            return head
        node = head
        pos_to_remove = list_len-n
        if pos_to_remove == 0:
            head = head.next
            return head
        counter = 0
        while node is not None:
            if counter == pos_to_remove-1:
                temp_node = node.next.next
                node.next = temp_node
                return head
            else:
                counter = counter + 1
                node = node.next
        return head

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

head_node1 = ListNode(1)
element_node1 = ListNode(2)
element_node2 = ListNode(3)
element_node3 = ListNode(4)
element_node4 = ListNode(5)

head_node1.next = element_node1
element_node1.next = element_node2
element_node2.next = element_node3
element_node3.next = element_node4

head_node2 = ListNode(1)
element_node = ListNode(2)
#head_node2.next = element_node

S = Solution()
node = S.removeNthFromEnd(head_node1, 2)
S.print_values(node)