class stack:
    container = list()

    def __init__(self) -> None:
        pass

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop()

# s = stack()
# s.push(10)
# s.push(20)
# s.push(30)

# print(s.pop())
# print(s.pop())