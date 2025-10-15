from collections import deque

class Stack:
    def __init__(self):
        self.stack = []
        self.len = 0
    
    def push(self, element):
        self.stack.append(element)
        self.len += 1

    def pop(self):
        if self.is_empty():         # verifica si la pila esta vacia
            print("El stack esta vacio, no se puede hacer pop")
            return None
        element = self.stack.pop()
        self.len -= 1
        return element

    def peek(self):
        if self.is_empty():         # verifica si la pila esta vacia
            print("El stack esta vacio, no hay elemento para peek")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0        

    def size(self):
        return self.len


class Queue:
    def __init__(self):
        self.queue = deque()
        self.len = 0
    
    def enqueue(self, element):
        self.queue.append(element)
        self.len += 1

    def dequeue(self):
        if self.is_empty():         # verifica si la cola esta vacia
            print("La cola esta vacia, no se puede hacer dequeue")
            return None
        element = self.queue.popleft()
