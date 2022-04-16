class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = self.get_num_from_list(l1)
        num2 = self.get_num_from_list(l2)
        total = num1 + num2
        dummyNode = resultNode = ListNode(-1)
        str_total = str(total)
        for i in range(len(str_total)):
            dummyNode.next = ListNode(int(str_total[i]))
            dummyNode = dummyNode.next
        return resultNode.next
        
    def get_num_from_list(self, l):
        if l:
            result = l.val
            l = l.next
        else: result = 0
        while l:
            result = result*10 + l.val
            l = l.next
        return result