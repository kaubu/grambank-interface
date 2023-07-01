""" 
[Values]
Values CSV Format is:

ID,Language_ID,Parameter_ID,Value,Code_ID,Comment,Source,Source_comment,Coders
...

where Language_ID is the glottocode ID
where ID's format is {Parameter_ID}-{Language_ID}

row[0] = ID                 GB031-abad1241
row[1] = Language_ID        abad1241
row[2] = Parameter_ID       GB031
row[3] = Value              0
row[4] = Code_ID            GB031-0
row[5] = Comment            Dual is marked by addition of the numeral two.
row[6] = Source             s_OaPaul_Gabadi[8]
row[7] = Source_comment     Oa & Paul 2013:8
row[8] = Coders             JLA
"""

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

import languages
from codes import codes

import csv
import sys

# import pandas as pd

maxInt = sys.maxsize

# Quick and dirty code
while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

GRAMBANK_VALUES = "./values3.csv"

DEFAULT_SORT = languages.test

def print_results(result):
    """ 
    languages_result = {
        "icel1247": {
            "language_name": "Icelandic",
            "code_value": 1,
            "code_description": "present",
            "comment": "…"
        },
    }
    """

    print("==[Detailed]==")
    for lang, metadata in result.items():
        print(
            f"{metadata['language_name']}: '{metadata['code_description']}'"
        )
        if metadata["comment"].strip() != "":
            print(f"  - {metadata['comment']}\n")

while True:
    parameter_id_input = input("Enter Parameter ID (e.g. GB020): ")
    print("Searching…")

    languages_result = {}

    """ 
    languages_result = {
        "META": {
            "frequency": {
                42: {"absent"},
                1: {"present"},
            }
        }
        "icel1247": {
            "language_name": "Icelandic",
            "code_value": 1,
            "code_description": "present",
            "comment": "…"
        },
    }
    """
    
    with open(
        GRAMBANK_VALUES,
        mode="r",
        newline="",
        encoding="utf8"
    ) as csvfile:
        csvreader = csv.reader(
            csvfile,
            delimiter = "\t",
            quotechar = "|",
        )

        is_newline = False
        newline_buffer = []

        for i, row in enumerate(csvreader):
            # If it is the column title row
            if i == 0: continue

            # print(f"row = {row}")

            # row = row[0].split(",")

            # print(f"row = {row}")
            # input("Cont?")

            """ 
            row[1] = Language_ID        abad1241
            row[2] = Parameter_ID       GB031
            row[3] = Value              0
            row[4] = Code_ID            GB031-0
            row[5] = Comment            Dual is marked by addition of the
                                        numeral two.
            """

            # Check if there are newlines and fix it
            if len(row) < 9:
                if is_newline:
                    newline_buffer += [r.strip() for r in row]
                    continue
                else:
                    newline_buffer = [r.strip() for r in row]
                    is_newline = True
                    continue
            elif len(row) == 9 and is_newline:
                row = newline_buffer + [r.strip() for r in row]
                is_newline = False
                newline_buffer = []

            language_id = row[1]
            parameter_id = row[2]
            value = row[3]
            code_id = row[4]
            comment = row[5]

            # If the language matches the section we're on
            if language_id in DEFAULT_SORT.keys():
                if parameter_id == parameter_id_input:
                    
                    # print(f"row = ===\n{row}\n===")
                    # print(f"row[1] = Language_ID = {row[1]}")
                    # print(f"row[2] = Parameter_ID = {row[2]}")
                    # print(f"row[3] = Value = {row[3]}")
                    # print(f"row[4] = Code_ID = {row[4]}")
                    # print(f"row[5] = Comment = {row[5]}")

                    if code_id not in codes: code_id = "UNKNOWN"

                    languages_result[language_id] = {
                        "language_name": DEFAULT_SORT[language_id]["name"],
                        "code_value": value,
                        "code_description": codes[code_id],
                        "comment": comment,
                    }
    
    print("Finished.")
    # print(f"\n[Languages]\n{languages}\n")
    print_results(languages_result)
    print()

    languages_result = {}