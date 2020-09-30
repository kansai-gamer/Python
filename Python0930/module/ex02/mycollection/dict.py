def same_value_dictionary(keys, value=1):
    return {keys: value for key in keys}

def random_value_dictionary(keys, start=1, end=9):
    from random import randint
    return {keys: randint(start, end) for key in keys}