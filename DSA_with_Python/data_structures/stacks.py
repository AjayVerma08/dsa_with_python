class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
    def isempty(self):
        return self.top is None

    def size(self):
        return self._size

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    def peak(self):
        if self.isempty():
            return "Empty Stack"
        else:
            return self.top.data

    def traverse(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def pop(self):
        if self.isempty():
            return "Empty Stack"
        else:
            data = self.top.data
            self.top = self.top.next
            self._size -= 1
            return data
# reversing a string with a stack
def reverse_string(text):
    s = Stack()
    for i in text:
        s.push(i)
    res = ''
    while not s.isempty():
        res = res + s.pop()

    print(res)
# text editor problem with stacks
def text_editor(text, pattern):
    u = Stack()
    r = Stack()

    for i in text:
        u.push(i)
    for i in pattern:
        if i == 'u':
            data = u.pop()
            r.push(data)
        else:
            data = r.pop()
            u.push(data)
    res = ''
    while not u.isempty():
        res = u.pop() + res
    print(res)

# celebrity problem with stack
def find_the_celeb(matrix):
    s = Stack()
    for i in range(len(matrix)):
        s.push(i)
    while s.size() >= 2:
        i = s.pop()
        j = s.pop()
        if matrix[i][j] == 0:
            s.push(i)
        else:
            s.push(j)
    celeb = s.pop()
    for i in range(len(matrix)):
        if i != celeb:
            if matrix[i][celeb] == 0 or matrix[celeb][i] == 1:
                print('No one is a celebrity')
                return
    print("The celebrity is ", celeb)

# balanced bracket problem using stacks
def balanced_parenthesis(expression):
     s = Stack()
     pairs = {')':'(', ']':'[', '}':'{'}
     for i in expression:
         if i in '({[':
             s.push(i)
         elif i in ')}]':
             if s.isempty() or s.pop() != pairs[i]:
                 # print(False)
                 return False
     # print(s.size() == 0)
     return s.size() == 0



