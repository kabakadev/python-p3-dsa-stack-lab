class Stack:
    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []  
        self.limit = limit  
    
    def isEmpty(self):
        return len(self.items) == 0  
    
    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)  
        else:
            return None
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()  
        else:
            return None
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1] 
        else:
            raise IndexError("Peek from empty stack")  
    
    def size(self):
        return len(self.items)  
    
    def full(self):
        return len(self.items) == self.limit 
    
    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1  
        else:
            return -1  
