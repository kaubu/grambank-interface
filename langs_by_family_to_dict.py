""" 
[Languages]
ID,Name,Macroarea,Latitude,Longitude,Glottocode,ISO639P3code,provenance,
Family_name,Family_level_ID,Language_level_ID,level,lineage

abad1241,Abadi,Papunesia,-9.03389,146.992,abad1241,,JLA_abad1241.tsv,
Austronesian,aust1307,abad1241,language,
aust1307/mala1545/cent2237/east2712/ocea1241/west2818/papu1253/peri1258/cent2070/west2850

row[0] = ID                     stan1293
row[1] = Name                   English
row[2] = Macroarea              Eurasia
row[3] = Latitude               53.0
row[4] = Longitude              -1.0
row[5] = Glottocode             stan1293
row[6] = ISO639P3code           
row[7] = provenance             JG-JLA-IC_stan1293.tsv
row[8] = Family_name            Indo-European
row[9] = Family_level_ID        indo1319
row[10] = Language_level_ID     stan1293
row[11] = level                 language
row[12] = lineage               indo1319/clas1257/germ1287/nort3152/west2793/nort3175/angl1264/angl1265/late1254/merc1242/macr1271

The relevant columns are:
row[0] = ID                     stan1293
row[1] = Name                   English
row[8] = Family_name            Indo-European
row[11] = level                 language / Check if it is a language
                                Possible values are: language, dialect, family
"""

""" 
This file pairs the ID with the Description, and exports it as a .py file
"""

import csv

INPUT = "languages.csv"
OUTPUT = "language_families.py"

languages = {}

with open(INPUT, mode="r", newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",", quotechar = "|")

    for i, row in enumerate(csvreader):
        # If it is the column row
        if i == 0: continue

        """ 
        row[0] = ID                     stan1293
        row[1] = Name                   English
        row[8] = Family_name            Indo-European
        row[11] = level                 language / Check if it is a language
                                        Possible values are: language, dialect,
                                        family
        """

        # codes[row[0]] = row[3]

        lang_id = row[0]
        name = row[1]
        family_name = row[8]
        level = row[11]

        if level == "dialect":
            continue
        elif level == "family":
            continue

        if family_name in languages:
            languages[family_name][lang_id] = {
                    name,
            }
        else:
            languages[family_name] = {
                lang_id: {
                    name,
                },
            }
        
        # languages[family_name][lang_id] = {
        #         name,
        # }

        # print(f"row = {row}")
        # input("Cont?")

# print(f"languages = {languages}")

input("Press ENTER to continue writing.\n")

with open(OUTPUT, mode="w", encoding="utf8") as f:
    f.write("language_families = {\n")

    for family, language in languages.items():
        f.write(f"    \"{family}\": {{\n")
    
        for k, v in languages[family].items():
            # print(f"k = {k}; v = {v}")
            # input("Cont?")

            f.write(f"        \"{k}\": {{\n")
            f.write(f"            \"name\": \"{list(v)[0]}\",\n")
            f.write("        },\n")
        
        f.write("    },\n")
    
    f.write("}")
