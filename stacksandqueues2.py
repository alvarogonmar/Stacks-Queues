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
        self.len -= 1
        return element

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
