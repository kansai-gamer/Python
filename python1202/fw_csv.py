import csv

data = [
    {"mach": 50, "eng":70},
    {"mach": 60, "eng":80},
    {"mach": 70, "eng":90},
]

file_name = "test2.csv"
with open(file_name, 'w') as f:
    writer = csv.writer(f, lineterminator="\n")
    for line in data:
        writer.writerow([line["mach"], line["eng"]])