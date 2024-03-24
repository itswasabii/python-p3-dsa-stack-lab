class Stack:

    def __init__(self, items = [], limit = 100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
       return len(self.items) == 0
    

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack is full")

    
    
    def empty(self):
        return len(self.items) == 0


    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty")
 

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit


    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        else:
            return -1
        