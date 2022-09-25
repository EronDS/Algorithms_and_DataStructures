
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self,value:int or float):
        self.head = Node(value)
        self.tail = self.head
        self.ns = [] 
        self.ordered = False
    def append(self,x:int or float):
        if self.head == None and self.tail == None:
            self.head = self.tail = Node(x)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(x)
        self.tail = current.next
        current.next.prev = current
        if current.next.value < current.next.prev.value: self.ordered=False

    def print_traversal_forward(self):
        if self.head == None and self.tail == None:return [None]
        self.nodes = [] 
        current = self.head
        while current.next:
            self.nodes.append(current.value)
            current = current.next
        self.nodes.append(current.value)
        return self.nodes
    def print_traversal_backwards(self):
        if self.head == None and self.tail == None:return [None]
        self.nodes = [] 
        current = self.tail
        while current.prev:
            self.nodes.append(current.value)
            current = current.prev
        self.nodes.append(current.value)
        return self.nodes    
    def sort(self):
        self.nodes = [] 
        current = self.head
        while current.next:
            self.nodes.append(current.value)
            current = current.next
        self.nodes.append(current.value)
        self.nodes = sorted(self.nodes)
        self.clean()
        for i in self.nodes:
            self.append(i)
        self.ordered=True
        return
    def clean(self):
        current = self.head
        while current.next:
            current = current.next
            current.next = None
            current.prev = None
        current.prev = None
        self.head = None
        self.tail = None
        return
    
    def find_value(self,value):
        if self.ordered:
            print('ordered')
            a = value - self.tail.value
            b = value - self.head.value
            if abs(a) < abs(b):
                print('searching through backwards traversal')
                current = self.tail 
                while current.prev:
                    if current.value == value:
                        return True
                    current = current.prev

            else: 
                print('searching through forward traversal')
                current = self.head
                while current.next:
                    if current.value == value:
                        return True
                    current = current.next
        else:
            print('unordered\nsearching through forward traversal')
            current = self.head
            while current.next:
                if current.value == value:return True
                current = current.next
        return False

import random
ll = LinkedList(1)
for i in [random.randint(0,100) for _ in range(10)]:
    ll.append(i)

print(*ll.print_traversal_forward())
print(*ll.print_traversal_backwards())
print(*ll.print_traversal_forward())
print(ll.find_value(20))