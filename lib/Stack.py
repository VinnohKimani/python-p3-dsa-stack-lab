class Stack:

    def __init__(self, items = [], limit = 100):
        if items is None:
          items = []

        self.items = list(items)    
        self.limit = limit


    def isEmpty(self):
        return len(self.items) == 0
    def push(self, item):
        # self.items.append(item)
        if not self.full():
          self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            return self.items[::-1].index(target)
        except ValueError:
            return -1
