frisian = {
    "west2354": {
        "name": "Western Frisian",
    },
}

anglic = {
    "stan1293": {
        "name": "English",
    },
    # Scots – There is no Scots language code
}

# Anglo-Frisian
anglo_frisian = anglic | frisian

dutch = {
    "dutc1256": {
        "name": "Dutch",
    },
}

# Low Franconian
low_franconian = dutch

## West Germanic
west_germanic = anglo_frisian | low_franconian

# North-West Germanic
north_west_germanic = {
    "icel1247": {
        "name": "Icelandic",
    },
    "faro1244": {
        "name": "Faroese",
    },
    # Norwegian. No Norwegian data
}

# North-East Germanic
north_east_germanic = {
    "dani1285": {
        "name": "Danish",
    },
    "swed1254": {
        "name": "Swedish",
    },
}

## North Germanic
north_germanic = north_west_germanic | north_east_germanic

# Hellenic
hellenic = {
    # "anci1242": {
    #     "name": "Ancient Greek",
    # }, # Commented because it's dead
    "mode1248": {
        "name": "Modern Greek",
    },
}

test = {
    "cent2127": {
        "name": "Central Alaskan Yupik",
    }
}

living_indo_european: {
    # "anci1242": {
    #     "name": "Ancient Greek",
    # },
    "arom1237": {
        "name": "Aromanian",
        "native_speakers": 470_000,
        "total_speakers": 210_000,
    },
    "awad1243": {
        "name": "Awadhi",
        "total_speakers": 4_400_000,
    },
    "baha1260": {
        "name": "Bahamas Creole English",
        "total_speakers": 400_000,
    },
    "bela1254": {
        "name": "Belarusian",
        "total_speakers": 11_400_000,
    },
    "beli1260": {
        "name": "Belize Kriol English",
        "total_speakers": 350_000,
    },
    # "berb1259": {
    #     "name": "Berbice Creole Dutch",
    # }, # Extinct since 2005 :(
    "bhoj1244": {
        "name": "Bhojpuri",
        "total_speakers": 51_000_000,
    },
    "bisl1239": {
        "name": "Bislama",
        "total_speakers": 210_000,
    },
    "bret1244": {
        "name": "Breton",
        "total_speakers": 226_000,
    },
    "bund1253": {
        "name": "Bundeli",
        "total_speakers": 5_600_000,
    },
    "camp1261": {
        "name": "Campidanese Sardinian",
        "total_speakers": 500_000,
    },
    "cent1972": {
        "name": "Central Kurdish",
        "total_speakers": 8_000_000,
    },
    # "clas1249": {
    #     "name": "Classical-Middle Armenian",
    # },
    "cors1241": {
        "name": "Corsican",
        "total_speakers": 150_000,
    },
    "czec1258": {
        "name": "Czech",
        "total_speakers": 10_700_000,
    },
    "dani1285": {
        "name": "Danish",
        "total_speakers": 6_000_000,
    },
    "dara1250": {
        "name": "Darai",
        "total_speakers": 20_000,
    },
    "doma1260": {
        "name": "Domaaki",
        "total_speakers": 340,
    },
    "dutc1256": {
        "name": "Dutch",
        "total_speakers": 30_000_000,
    },
    "faro1244": {
        "name": "Faroese",
        "total_speakers": 72_000,
    },
    "gali1258": {
        "name": "Galician",
        "total_speakers": 2_400_000,
    },
    "gheg1238": {
        "name": "Gheg Albanian",
        "total_speakers": 4_100_000,
    },
    "gura1251": {
        "name": "Gurani / Gorani / Hawrami",
        "total_speakers": 350_000,
    },
    "hait1244": {
        "name": "Haitian / Haitian Creole",
        "total_speakers": 12_000_000,
    },
    # "hier1240": {
    #     "name": "Hieroglyphic Luwian",
    # },
    "hind1269": {
        "name": "Hindi",
        "total_speakers": 592_000_000,
    },
    "icel1247": {
        "name": "Icelandic",
        "total_speakers": 357_069,
    },
    "iris1253": {
        "name": "Irish",
        "total_speakers": 2_272_597,
    },
    "iron1242": {
        "name": "Iron Ossetian",
        "total_speakers": 511_958,
    },
    "ital1282": {
        "name": "Italian",
        "total_speakers": 6_800_000,
    },
    "jama1262": {
        "name": "Jamaican Creole English",
        "total_speakers": 3_200_000,
    },
    "kash1277": {
        "name": "Kashmiri",
        "total_speakers": 7_100_000,
    },
    "konk1267": {
        "name": "Konkan Marathi / Maharashtr Konkani",
        "total_speakers": 2_400_000,
    },
    "kumz1235": {
        "name": "Kumzari",
        "total_speakers": 6030,
    },
    "lamb1269": {
        "name": "Lambadi",
        "total_speakers": 5_000_000,
    },
    # "lati1261": {
    #     "name": "Latin",
    # },
    "latv1249": {
        "name": "Latvian",
        "total_speakers": 1_500_000,
    },
    "limo1249": {
        "name": "Limonese Creole",
        "total_speakers": 55_000,
    },
    "lith1251": {
        "name": "Lithuanian",
        "total_speakers": 3_000_000,
    },
    "lomb1257": {
        "name": "Lombard",
        "total_speakers": 3_800_000,
    },
    "mace1250": {
        "name": "Macedonian",
        "total_speakers": 3_500_000,
    },
    "maga1260": {
        "name": "Magahi",
        "total_speakers": 12_600_000,
    },
    "mait1250": {
        "name": "Maithili",
        "total_speakers": 34_000_000,
    },
    "mara1378": {
        "name": "Marathi",
        "total_speakers": 95_000_000,
    },
    "mode1248": {
        "name": "Modern Greek",
        "total_speakers": 13_400_000,
    },
    "nepa1254": {
        "name": "Nepali",
        "total_speakers": 25_000_000,
    },
    "nica1252": {
        "name": "Nicaragua Creole English / Miskito Coast Creole",
        "total_speakers": 18_000,
    },
    "nucl1235": {
        "name": "Eastern Armenian",
        "total_speakers": 3_800_000,
    },
    "occi1239": {
        "name": "Occitan",
        "total_speakers": 800_000,
    },
    # "olde1238": {
    #     "name": "Old English (ca. 450-1100)",
    # },
    "oriy1255": {
        "name": "Odia",
        "total_speakers": 39_000_000,
    },
    "panj1256": {
        "name": "Eastern Panjabi / Standard Punjabi",
        "total_speakers": 113_000_000,
    },
    "piji1239": {
        "name": "Pijin",
        "total_speakers": 324_000,
    },
    "plau1238": {
        "name": "Plautdietsch",
        "total_speakers": 450_000,
    },
    "poli1260": {
        "name": "Polish",
        "total_speakers": 45_000_000,
    },
    "port1283": {
        "name": "Portuguese",
        "total_speakers": 260_000_000,
    },
    "pras1239": {
        "name": "Prasun / Wasi-wari",
        "total_speakers": 8000,
    },
    "roma1326": {
        "name": "Romansh",
        "total_speakers": 60_000,
    },
    "russ1263": {
        "name": "Russian",
        "total_speakers": 260_000_000,
    },
    "sana1297": {
        "name": "San Andres Creole English / San Andrés—Providencia creole",
        "total_speakers": 12_000,
    },
    "sara1340": {
        "name": "Saramaccan",
        "total_speakers": 90_000,
    },
    "sici1248": {
        "name": "Sicilian",
        "total_speakers": 4_700_000,
    },
    "slov1268": {
        "name": "Slovenian / Slovene",
        "total_speakers": 2_500_000,
    },
    "sout1528": {
        "name": "Serbian-Croatian-Bosnian / Serbo-Croatian",
        "total_speakers": 19_000_000,
    },
    "sout2649": {
        "name": "Southern Pashto",
        "total_speakers": 16_893_700,
    },
    "stan1289": {
        "name": "Catalan",
        "total_speakers": 9_200_000,
    },
    "stan1290": {
        "name": "French",
        "native_speakers": 80_000_000,
        "total_speakers": 270_000_000,
    },
    "stan1293": {
        "name": "English",
        "native_speakers": 372_900_000,
        "total_speakers": 1_080_000_000,
    },
    "swed1254": {
        "name": "Swedish",
        "native_speakers": 10_000_000,
        "total_speakers": 13_000_000,
    },
    "tokp1240": {
        "name": "Tok Pisin",
        "native_speakers": 130_000,
        "total_speakers": 4_130_000,
    },
    "torr1261": {
        "name": "Torres Strait-Lockhart River Creole / Torres Strait Creole",
        "native_speakers": 30_000,
        "total_speakers": 30_000,
    },
    "tosk1239": {
        "name": "Northern Tosk Albanian",
        "native_speakers": 1_800_000,
        "total_speakers": 1_800_000,
    },
    "ukra1253": {
        "name": "Ukrainian",
        "native_speakers": 27_000_000,
        "total_speakers": 32_800_000,
    },
    "wels1247": {
        "name": "Welsh",
        "native_speakers": 657_185,
        "total_speakers": 657_185,
    },
    "west2354": {
        "name": "Western Frisian / West Frisian",
        "native_speakers": 470_000,
        "total_speakers": 470_000,
    },
    "west2369": {
        "name": "Western Farsi / Iranian Persian",
        "native_speakers": 55_600_000,
        "total_speakers": 55_600_000,
    },
    "west2386": {
        "name": "Western Panjabi",
        "native_speakers": 34_520_000,
        "total_speakers": 34_520_000,
    },
}