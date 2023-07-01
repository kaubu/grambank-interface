""" 
[Codes]
The Codes CSV helps understand what the number means.

ID,Parameter_ID,Name,Description
GB020-0,GB020,0,absent

row[0] = ID                 GB020-0
row[1] = Parameter_ID       GB020
row[2] = Name               0
row[3] = Description        absent
"""

""" 
This file pairs the ID with the Description, and exports it as a .py file
"""

import csv

INPUT = "codes.csv"
OUTPUT = "codes.py"

codes = {}

with open(INPUT, mode="r", newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",", quotechar = "|")

    for i, row in enumerate(csvreader):
        # If it is the column row
        if i == 0: continue

        # row = row[0].split(",")

        # print(f"row = {row}")
        # input("Cont?")

        codes[row[0]] = row[3]

with open(OUTPUT, mode="w", encoding="utf8") as f:
    f.write("codes = {\n")
    
    for k, v in codes.items():
        f.write(f"    \"{k}\": \"{v}\",\n")
    
    f.write("}")
