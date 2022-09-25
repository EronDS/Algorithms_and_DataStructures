import sys
import os
from deque import Deque,Node

class Queue:
    def __init__(self,element):
        self.queue = Deque(element)
    def enqueue(self,element): return self.queue.addBack(element)
    def dequeue(self): 
        if self.queue.tail.prev:
            return self.queue.removeFront()
        else: 
            self.queue.tail = None 
            self.queue.head = self.queue.tail
    def peek(self): 
        if self.queue.tail: return self.queue.peekFront()
        else:return(print('Empty'))
