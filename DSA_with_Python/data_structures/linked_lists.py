"""Implementing a Linked List"""
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        # Creating an empty linked list
        self.head = None
        # Count of the nodes in LL
        self.n = 0
    def __len__(self):
        """return the length of the list"""
        return  self.n

    def insert_head(self, value):
        """insert data into the head"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n = self.n + 1

    def append(self,value):
        """insert data at the tail"""
        new_node = Node(value)
        # check if the LL is empty or not
        if self.head is None:
            self.head = new_node
            self.n = self.n + 1
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        self.n = self.n + 1
    def insert_after(self, after, value):
        """insert data in the middle/after a value/item"""
        new_node = Node(value)
        curr = self.head
        while curr is not None:
            if curr.data == after:
                break
            curr = curr.next
        # check if the curr is not None
        if curr is not None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
            return None
        else:
            return 'Item not found'

    def __str__(self):
        """converting data to string for printing"""
        curr = self.head
        result = ''
        while curr is not None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]
    def clear(self):
        """deleting all the data"""
        self.head = None
        self.n = 0

    def delete_head(self):
        """removing the head from List"""
        if self.head is None:
            return "Empty LL"
        self.head = self.head.next
        self.n = self.n - 1
        return None

    def pop(self):
        """removes the tail from the list"""
        if self.head is None:
            return "Empty LL"
        curr = self.head
        if curr.next is None:
            return self.delete_head()
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
        self.n = self.n - 1
        return None

    def remove(self, value):
        """remove item from the middle or from head or tail"""
        if self.head is None:
            return 'Empty LL'
        if self.head.data == value:
            return self.delete_head()
        curr = self.head
        while curr.next is not None:
            if curr.next.data == value:
                break
            curr = curr.next
        if curr.next is None:
            return 'Item not found'
        else:
            curr.next = curr.next.next
            self.n = self.n - 1
        return None
    def deleteByIndex(self, index):
        value = self.__getitem__(index)
        return self.remove(value)

    def search(self, item):
        """look for an item in the list"""
        curr = self.head
        pos = 0
        while curr is not None:
            if curr.data == item:
                print(f"index:{pos}")
                return pos
            curr = curr.next
            pos += 1
        return 'Not found'

    def __getitem__(self, index):
        """look for an item based on it's index"""
        curr = self.head
        pos = 0
        while curr is not None:
            if pos == index:
                print(curr.data)
                return curr.data
            curr = curr.next
            pos += 1
        error = "IndexError: Index out of range"
        return print("IndexError: Index out of range"), error


L = LinkedList()
