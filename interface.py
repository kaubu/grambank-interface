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
from language_families import language_families

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

# DEFAULT_SORT = languages.test
# DEFAULT_SORT = language_families["Indo-European"]
DEFAULT_SORT = languages.living_indo_european

# Sort by keys in descending order
def sort_by_keys(dictionary):
    return dict(sorted(dictionary.items(), key=lambda x:x[1], reverse=True))

def calculate_weights(result) -> (dict, dict):
    """ 
    native_weights = {
        "present": 48.24,
        "absent": 23.41,
        "unknown": 45,
    }
    """

    native_weights = {}
    total_weights = {}

    for lang, metadata in result.items():
        code_description = metadata["code_description"]

        if code_description in native_weights:
            native_weights[code_description] += metadata["native_weight"]
        else:
            native_weights[code_description] = metadata["native_weight"]
        
        if code_description in total_weights:
            total_weights[code_description] += metadata["total_weight"]
        else:
            total_weights[code_description] = metadata["total_weight"]
    
    native_weights = sort_by_keys(native_weights)
    total_weights = sort_by_keys(total_weights)

    return (native_weights, total_weights)

def calculate_frequency(result) -> dict:
    frequency = {}

    for lang, metadata in result.items():
        code_description = metadata["code_description"]

        if code_description in frequency:
            frequency[code_description] += 1
        else:
            frequency[code_description] = 1
    
    frequency = sort_by_keys(frequency)
    
    return frequency

def print_results(result):
    """ 
    languages_result = {
        "icel1247": {
            "language_name": "Icelandic",
            "code_value": 1,
            "code_description": "present",
            "comment": "…",
            "native_weight": 0.12,
            "total_weight": 0.9
        },
    }
    """

    print("==[Overview]==")
    native_weights, total_weights = calculate_weights(result)
    # print(f"native_weights = {native_weights}")
    # print(f"total_weights = {total_weights}")

    print("[Native Speakers]")
    for weight_name, weight_value in native_weights.items():
        print(f"* {weight_name}: {weight_value}% of speakers")

    print("[Total Speakers]")
    for weight_name, weight_value in total_weights.items():
        print(f"* {weight_name}: {weight_value}% of speakers")
    
    print("[Frequency by Language]")
    frequency = calculate_frequency(result)
    for code, frequency_value in frequency.items():
        print(f"* {code}: {frequency_value}")

    print("==[Detailed]==")
    for lang, metadata in result.items():
        print(
            f"{metadata['language_name']}: '{metadata['code_description']}'"
        )
        if metadata["comment"].strip() != "":
            print(f"  - {metadata['comment']}\n")

while True:
    print("================================================================")

    parameter_id_input = input("Enter Parameter ID (e.g. GB020): ")
    print("Searching…")

    languages_result = {}

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
                        "native_weight": 
                            DEFAULT_SORT[language_id]["native_weight"],
                        "total_weight":
                            DEFAULT_SORT[language_id]["total_weight"],
                    }
    
    print("Finished.")
    # print(f"\n[Languages]\n{languages}\n")
    print_results(languages_result)
    print()

    languages_result = {}