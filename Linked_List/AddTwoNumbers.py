class ListNode(object):
    def __init__(self, data_value):
        self.val = data_value
        self.next = None

class Solution(object):
    '''Worst case Complexities: Space: O(1), time: O(N) where N being thesize of the longest list'''
    def addTwoNumbers(self, l1, l2):
        result = head = ListNode(-1)
        num1 = 0
        num2 = 0
        counter = 0
        while l1 is not None:
            num1 = num1 + l1.val * (10**counter)
            l1 = l1.next
            counter = counter + 1
        counter = 0
        while l2 is not None:
            num2 = num2 + (l2.val) * (10**counter)
            l2 = l2.next
            counter = counter + 1
        sum = num1 + num2
        if sum==0:
            return ListNode(0)
        while sum!=0:
            head.next = ListNode(sum%10)
            sum = sum // 10
            head = head.next
        return result.next

    ''' This method is just for testing '''
    def print_values(self, node):
        while node is not None:
            print(node.val)
            node = node.next

head_node1 = ListNode(2)
element_node1 = ListNode(4)
element_node2 = ListNode(3)

head_node1.next = element_node1
element_node1.next = element_node2

head_node2 = ListNode(5)
element_node7 = ListNode(6)
element_node8 = ListNode(4)

head_node2.next = element_node7
element_node7.next = element_node8

head_node3 = ListNode(0)
head_node4 = ListNode(0)

S = Solution()
node = S.addTwoNumbers(head_node3, head_node4)
S.print_values(node)