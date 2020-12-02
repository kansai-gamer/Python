import json

data = [
    {"mach": 50, "eng":70},
    {"mach": 60, "eng":80},
    {"mach": 70, "eng":90},
]

file_name = "test.json"
with open(file_name, 'w') as f:
    json.dump(data, f, indent=4)