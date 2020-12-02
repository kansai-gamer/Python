import json

file_name = "test.json"

with open(file_name, "r") as f:
    data = json.load(f)
    print(data)