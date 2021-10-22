class queue:
    container = list()
    def __init__(self, val):
        self.container.append(val)

    def insert(self, val):
        self.container.append(val)

    def dequeue(self):
        return self.container.pop(0)

q = queue(10)

q.insert(20)
q.insert(40)

print(q.dequeue())
print(q.dequeue())