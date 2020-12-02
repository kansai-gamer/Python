data = [
    {"mach": 50, "eng":70},
    {"mach": 60, "eng":80},
    {"mach": 70, "eng":90},
]

file_name = "test.csv"
with open(file_name, 'w') as f:
    for line in data:
        f.write(str(line["mach"]) + "," + str(line["eng"]) + "\n")