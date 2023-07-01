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

GRAMBANK_VALUES = "./values2.csv"

DEFAULT_SORT = languages.west_germanic

while True:
    parameter_id_input = input("Enter Parameter ID: ")

    languages = {}

    """ 
    languages = {
        "icel1247": "1",
    }
    """
    
    with open(
        GRAMBANK_VALUES,
        mode="r",
        # newline="\r\n",
        encoding="utf8"
    ) as csvfile:
        csvreader = csv.reader(
            csvfile,
            delimiter = ",",
            quotechar = "|",
            dialect=csv.excel_tab
        )

        for i, row in enumerate(csvreader):
            # If it is the column title row
            if i == 0: continue

            print(f"row = {row}")

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

            language_id = row[1]
            parameter_id = row[2]
            value = row[3]
            code_id = row[4]

            # If the language matches the section we're on
            if language_id in DEFAULT_SORT:
                if parameter_id == parameter_id_input:
                    languages[language_id] = codes[code_id]

print(f"[Languages]\n{languages}\n")