i = 15
b = i.to_bytes(2, byteorder="big")
print(b)

bit_length = i.bit_length()
print(bit_length)