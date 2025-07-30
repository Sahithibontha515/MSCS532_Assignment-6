from Array import Array

''' Created Stack using the Array'''
class Stack:
    def __init__(self):
        self.data = Array()
    
    def push(self, value):
        self.data.insert(0, value)
    
    def pop(self):
        return self.data.delete(0)
    
    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)
    
    def peek(self):
        return self.data.get(0)
    
    def is_empty(self):
        return len(self.data) == 0
    
class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0) if self.data else None

    def is_empty(self):
        return len(self.data) == 0
