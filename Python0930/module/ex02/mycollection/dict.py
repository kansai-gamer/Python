def same_value_dictionary(keys, value=1):
    return [value for _ in range(keys)]

def random_value_dictionary(keys, start=1, end=9):
    from random import randint
    return [randint(start, end) for _ in range(keys)]