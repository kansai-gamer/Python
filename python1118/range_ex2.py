class MyInterator:
    def __init__(self, names):
        self.names = names
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 3:
            raise StopIteration()
        value = self.index
        self.index += 1
        return (value, names[value])

names = ["Alice", "Bob", "Carol"]
for i, v in MyInterator(names):
    print(i, v)