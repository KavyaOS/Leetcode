class ListNode(object):
    def __init__(self, data_value):
        self.val = data_value
        self.next = None

class Solution(object):
    '''Worst case Complexities: Space: O(1), time: O(N)'''
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        given_list = head
        list_values = []
        while given_list is not None:
            list_values.append(given_list.val)
            given_list = given_list.next
        reversed_list = self.reverseList(head)
        counter = 0
        while reversed_list is not None:
            if reversed_list.val != list_values[counter]:
                return False
            counter = counter + 1
            reversed_list = reversed_list.next
        return True

    def reverseList(self, list_head):
        if list_head is None or list_head.next is None:
            return list_head
        black_node = list_head
        while black_node is not None and black_node.next is not None:
            next_to_black = black_node.next
            black_node.next = next_to_black.next
            next_to_black.next = list_head
            list_head = next_to_black
        return list_head

    ''' This method is just for testing '''
    def print_values(self, node):
        while node is not None:
            print(node.val)
            node = node.next

head_node1 = ListNode(1)
element_node1 = ListNode(1)
element_node2 = ListNode(2)
element_node3 = ListNode(1)

head_node1.next = element_node1
element_node1.next = element_node2
element_node2.next = element_node3

head_node2 = ListNode(1)
element_node7 = ListNode(2)
element_node8 = ListNode(2)
element_node9 = ListNode(1)

head_node2.next = element_node7
element_node7.next = element_node8
element_node8.next = element_node9

S = Solution()
print(S.isPalindrome(head_node1))
# node = S.reverseList(head_node1)
# S.print_values(node)