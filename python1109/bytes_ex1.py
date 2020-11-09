numbers = [1, 2, 4, 8, 16]

numbers_bytes_list = [number.to_bytes(1,byteorder="big") for number in numbers]

print(numbers_bytes_list)