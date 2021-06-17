from typing import Iterator


class ListNode(object):
    def __init__(self, data_value):
        self.data_value = data_value
        self.next_node = None

class MyLinkedList(object):
    def __init__(self, head):
        self.head = head

    def get(self, index):
        counter = 0
        node = self.head
        while node is not None:
            if counter == index:
                return node.data_value
            node = node.next_node
            counter = counter + 1
        return -1
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """

    def addAtHead(self, val):
        node = ListNode(val)
        node.next_node = self.head
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        

    def addAtTail(self, val):
        node = ListNode(val)
        iterator = self.head
        while iterator.next_node is not None:
            iterator = iterator.next_node
        iterator.next_node = node
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        

    def addAtIndex(self, index, val):
        counter = 0
        node = ListNode(val)
        iterator = self.head
        while iterator is not None:
            if counter == index:
                temp_node = iterator.next_node
                iterator.next_node = node
                node.next_node = temp_node
                break
            else:
                iterator = iterator.next_node

        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def deleteAtIndex(self, index):

        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
    
    def print_values(self):
        node = self.head
        while node is not None:
            print(node.data_value)
            node = node.next_node

head_node = ListNode(3)
element_node1 = ListNode(2)
element_node2 = ListNode(0)
element_node3 = ListNode(-4)

head_node.next_node = element_node1
element_node1.next_node = element_node2
element_node2.next_node = element_node3
#element_node3.next_node = element_node1

my_list = MyLinkedList(head_node)
print(my_list.get(2))
my_list.addAtHead(5)
my_list.print_values()