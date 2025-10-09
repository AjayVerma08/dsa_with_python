"""Implementing a dynamic array"""

import ctypes
class Mylist:
    def __init__(self):
        self.size = 1
        self.n = 0
        # C type array with size = self.size
        self.A = self.__make_array(self.size)

    def __str__(self):
        """converts all the items in the array to strings"""
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'

    def __getitem__(self, index):
        """fetches the item of based on given index"""
        if 0<= index < self.n:
             return self.A[index]
        else:
            return 'IndexError - Index out of range'



    def __make_array(self, capacity):
        """
        Creates the C type static and referential array using input capacity or size
        """
        return (capacity*ctypes.py_object)()

    def __len__(self):
        """returns the n i.e the number of items or length of the array"""
        return self.n

    def __append__(self, item):
        """adds an item to the array"""
        if self.n == self.size:
            self.resize(self.size*2)

        self.A[self.n] = item
        self.n += 1

    def pop(self):
        """deletes the last item from the array"""
        if self.n == 0:
            return 'Empty List'
        print(self.A[self.n-1])
        self.n = self.n - 1
        return None

    def clear(self):
        """emptys the whole array"""
        self.size = 1
        self.n = 0

    def find(self, item):
        """finds the item in the array and returns it"""
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError - Value not in list'

    def insert(self, index, item):
        """inserting an item to the array based on the index and given item"""
        if 0 <= index < self.n:
            if self.n == self.size:
                self.resize(self.size*2)
            for i in range(self.n, index, -1):
                self.A[i] = self.A[i-1]
            self.A[index] = item
            self.n = self.n + 1
            return None
        else:
            return 'IndexError - Index out of range'

    def remove(self, item):
        """removes the specific item from the array"""
        index = self.find(item)
        if type(index) == int:
            self.__delitem__(index)
            return None
        else:
            return index

    def __delitem__(self, index):
        """deletes the specific item from the array based on given index"""
        if 0 <= index < self.n:
            for i in range(index, self.n-1):
                self.A[i] = self.A[i+1]
            self.n = self.n - 1

    def resize(self, new_capacity):
        """increases the size of the array for specific functionality such as adding new data if the array is full"""
        b = self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            b[i] = self.A[i]
        self.A = b


L = Mylist()
