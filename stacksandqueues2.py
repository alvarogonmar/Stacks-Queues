from collections import deque

class Stack:
    def __init__(self):
        self.stack = []
        self.len = 0
    
    def push(self, element):
        self.stack.append(element)
        self.len += 1

    def pop(self):
        element = self.stack.pop()
