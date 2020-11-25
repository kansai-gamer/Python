class Alphabet:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKMNLOPQRSTUVWXYZ"
        self.lower = False
        self.index = 0

    def __len__(self):
        return len(self.alphabet)

    def __getitem__(self,key):
        return self.alphabet[key]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self):
            raise StopIteration()

        value = self.alphabet[self.index]
        self.index += 1
        return value

    def show(self):
        if self.lower == True:
            print(self.alphabet.lower())
        else:
            print(self.alphabet)
    
    def set_lower(self):
        self.lower = True


alphabet = Alphabet()

x = iter(alphabet)
a = next(x)
print(a)
b = next(x)
print(b)
c = next(x)
print(c)

print(alphabet)

print(x)

print(alphabet == x)
# for x in alphabet:
#     print(x)

# for i in range(len(alphabet)):
#     print(alphabet[i])

# x = len(alphabet)
# print(x)

# a = alphabet[0]
# print(a)
# z = alphabet[25]
# print(z)