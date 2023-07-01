frisian = [
    "west2354" # West(ern) Frisian
]

anglic = [
    "stan1293", # English
    #"", # Scots – There is no Scots language code
]

# Anglo-Frisian
anglo_frisian = anglic + frisian

dutch = [
    "dutc1256", # Dutch
]

# Low Franconian
low_franconian = dutch

## West Germanic
west_germanic = anglo_frisian + low_franconian

# North-West Germanic
north_west_germanic = [
    "icel1247", # Icelandic
    "faro1244", # Faroese
    # "", # Norwegian. No Norwegian data
]

# North-East Germanic
north_east_germanic = [
    "dani1285", # Danish
    "swed1254", # Swedish
]

## North Germanic
north_germanic = north_west_germanic + north_east_germanic



# Hellenic
hellenic = [
    # "anci1242", # Ancient Greek. Commented because it's dead
    "mode1248", # Modern Greek
]