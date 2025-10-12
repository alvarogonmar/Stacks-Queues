from collections import deque

class Stack:
    def __init__(self):
        self.stack = []
        self.len = 0
    
    def push(self, element):
