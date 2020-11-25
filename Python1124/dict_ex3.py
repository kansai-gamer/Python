my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
except_keys = ["key1", "key3", "key5"]

for except_key in except_keys:
    del my_dict[except_key]

print(my_dict)