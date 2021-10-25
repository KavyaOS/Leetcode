class ListNode(object):
    def __init__(self, data_value):
        self.val = data_value
        self.next = None

class Solution(object):
    '''Worst case Complexities: Space: O(1), time: O(N) where N being thesize of the longest list'''
    def addTwoNumbers(self, l1, l2):
        num1 = self.num_from_list(l1)
        num2 = self.num_from_list(l2)
        sum = num1 + num2
        return self.make_list_from_num(sum)

    def make_list_from_num(self, num):
        result = head_node = ListNode(-1)
        if num==0: return ListNode(0)
        while num!=0:
            head_node.next = ListNode(num % 10)
            head_node = head_node.next
            num = num // 10
        return result.next
            
    def num_from_list(self, list):
        num = 0
        counter = 0
        while list is not None:
            num = num + list.val * (10**counter)
            list = list.next
            counter = counter + 1
        return num

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