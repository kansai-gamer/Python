class AlphabetIterator:
    def __init__(self, start, stop, step=1):
        self.index = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if     

for v in AlphabetIterator():
    print(v, end="")
print()