class ListNode(object):
    def __init__(self, data_value):
        self.data_value = data_value
        self.next_node = None

class MyLinkedList(object):
    def __init__(self):
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        counter = 0
        node = self.head
        while node is not None:
            if counter == index:
                return node.data_value
            node = node.next_node
            counter = counter + 1
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = ListNode(val)
        node.next_node = self.head
        self.head = node
        
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        node = ListNode(val)
        iterator = self.head
        if self.head is None:
            self.head = node
            return
        while iterator.next_node is not None:
            iterator = iterator.next_node
        iterator.next_node = node

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        counter = 0
        node = ListNode(val)
        iterator = self.head
        if self.head is None:
            self.head = node
            return
        if index == 0:
            node.next_node = self.head
            self.head = node
            return
        while iterator is not None:
            if counter == index-1:
                temp_node = iterator.next_node
                iterator.next_node = node
                node.next_node = temp_node
                break
            else:
                iterator = iterator.next_node
                counter = counter + 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        node = temp_node = self.head
        counter = 0
        if index == 0:
            self.head = self.head.next_node
            return
        while node is not None:
            if counter == index:
                while temp_node.next_node != node:
                    temp_node = temp_node.next_node
                temp_node.next_node = node.next_node
                break
            else:
                counter = counter + 1
                node = node.next_node
    
    '''method below is just for testing purpose'''
    def print_values(self):
        node = self.head
        while node is not None:
            print(node.data_value)
            node = node.next_node

'''head_node = ListNode(3)
element_node1 = ListNode(2)
element_node2 = ListNode(0)
element_node3 = ListNode(-4)

head_node.next_node = element_node1
element_node1.next_node = element_node2
element_node2.next_node = element_node3
#element_node3.next_node = element_node1'''

my_list = MyLinkedList()
#my_list.head = head_node
#print(my_list.get(2))
'''my_list.addAtHead(1)
#my_list.print_values()
my_list.addAtTail(3)
#my_list.print_values()
my_list.addAtIndex(1, 2)
my_list.print_values()
my_list.deleteAtIndex(0)
#my_list.print_values()'''

my_list.addAtIndex(0, 10)
my_list.addAtIndex(0, 20)
my_list.addAtIndex(1, 30)
#print(my_list.get(1))
my_list.print_values()